/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "adc.h"
#include "i2c.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "uart_handler.h"
#include "ring_buffer.h"
#include "liquidcrystal_i2c.h"

//#include "i2c-lcd.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define DEBOUNCE_TIME 50
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
volatile uint32_t pulse_duration = 0;
volatile uint8_t capture_done = 0;

uint32_t lastDebounceTime = 0;
GPIO_PinState lastPinState = GPIO_PIN_SET;

char uart_buffer[50];
RingBuffer UART_RingBuffer_Tx;
char RingBufferData_Tx[1024];
RingBuffer UART_RingBuffer_Rx;
char RingBufferData_Rx[1024];

char Response_Rx[1024];
uint8_t uart_rx_buffer;

uint8_t readyToRead;
uint8_t readyToSend;

char result[5];
char key_check[5];
char pass[5] = {'5', '0', '8', '2', '\0'};
char binary[5];
char binary_check[6];
char binary_pass[6] = {'1', '1', '0', '0', '1', '\0'};

uint16_t adcValue = 0;
uint8_t keyb = 1;
uint8_t diode = 0;
uint8_t volume = 0;

void HAL_UART_TxCpltCallback(UART_HandleTypeDef *huart)
{
  if (huart == &huart2) {
  }
}

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
  if (huart == &huart2) {
	  char_append(uart_rx_buffer);
    HAL_UART_Receive_IT(&huart2, &uart_rx_buffer, 1);
  }
}

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{

	if(htim==&htim1)
	{

	}
}


/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */
  RingBuffer_Init(&UART_RingBuffer_Tx, &RingBufferData_Tx, 1024);
  RingBuffer_Init(&UART_RingBuffer_Rx, &RingBufferData_Rx, 1024);
  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART2_UART_Init();
  MX_I2C1_Init();
  MX_TIM2_Init();
  MX_TIM1_Init();
  MX_ADC2_Init();
  /* USER CODE BEGIN 2 */
  HD44780_Init(2);
  HD44780_Clear();
  HD44780_SetCursor(0,0);
  HD44780_PrintStr("ON THE");
  HD44780_SetCursor(10,1);
  HD44780_PrintStr("OTHER SIDE");
  HAL_Delay(2000);
  HAL_TIM_Base_Start_IT(&htim1);
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  readyToRead = 0;
  readyToSend = 0;

  HAL_UART_Receive_IT(&huart2, &uart_rx_buffer, 1);


  HAL_TIM_IC_Start(&htim2, TIM_CHANNEL_1);
  HAL_TIM_IC_Start(&htim2, TIM_CHANNEL_2);
  HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_3);

  HAL_Delay(1000);

  uint32_t cursor = 0;
  uint32_t counter = 0;

  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */

     HAL_ADC_Start(&hadc2);
     if (HAL_ADC_PollForConversion(&hadc2, 1000) == HAL_OK)
     {
         adcValue = HAL_ADC_GetValue(&hadc2);
         counter = counter + 1;
         if ((adcValue < 200 || adcValue > 400) && counter > 2){
        	 volume = 1;
         }
     }
     HAL_ADC_Stop(&hadc2);


	 uint32_t start = HAL_TIM_ReadCapturedValue(&htim2, TIM_CHANNEL_1);
	 uint32_t stop = HAL_TIM_ReadCapturedValue(&htim2, TIM_CHANNEL_2);

	 uint32_t distance = (stop - start) / 58.0f;
	 HAL_Delay(1000);

	 char binary_buff[32];
	 if (strlen(binary_buff) == 5)
	 {
		 strcpy(binary_check, binary_buff);
	 }

	 if (HAL_GPIO_ReadPin(GPIOB, RESET_Pin) == GPIO_PIN_RESET || strlen(binary_buff) == 6)
	 {
		 HD44780_Clear();
		 binary_buff[0] = '\0';
		 binary_check[0] = '\0';
		 cursor = 0;
	 }

	 if (HAL_GPIO_ReadPin(GPIOB, SET_Pin) == GPIO_PIN_RESET)
	 {
		 HD44780_SetCursor(cursor,0);
		 if (distance < 15)
		 {
			 HD44780_PrintStr("1");
			 strcat(binary_buff, "1");
		 }
		 else
		 {
			 HD44780_PrintStr("0");
			 strcat(binary_buff, "0");
		 }
		 cursor = cursor + 1;
	 }

	 GPIO_PinState currentPinState = HAL_GPIO_ReadPin(CIRC_GPIO_Port, CIRC_Pin);

	 if (currentPinState != lastPinState)
	 {
		 lastDebounceTime = HAL_GetTick();
	 }

	 if ((HAL_GetTick() - lastDebounceTime) > DEBOUNCE_TIME)
	 {
		 if (currentPinState == GPIO_PIN_RESET)
	     {
	         HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
	         diode = 1;
	      }
	      else
	      {
	    	 HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
	    	 diode = 0;
	      }
	 }

	 lastPinState = currentPinState;

	 if (keyb == 1)
	 {
		 HD44780_Clear();
		 strcat(result, read_keyboard());
		 HD44780_PrintStr(result);
	 }

	 if(strlen(result) == 4)
  	 {
  		 strcpy(key_check, result);
  	 }

	 if(strlen(result) == 5 || read_keyboard() == "C")
	 {
		 result[0] = '\0';
		 HD44780_Clear();
	 }

	 if(readyToRead){
	     UART_ReadResponse();
	     readyToRead = 0;
	 }
	 if (readyToSend)
	 {
		 char toSend[32];

		 if (readyToSend == 1)
		 {
			 uint16_t finalSize = sprintf(toSend, "diode is on\r\n");
			 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
		 }
		 else if (readyToSend == 2)
		 {
			 if(strcmp(key_check, pass) == 0)
			 {
				 uint16_t finalSize = sprintf(toSend, "OK\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
				 HD44780_Clear();
				 keyb = 0;
			 }
			 else
			 {
				 uint16_t finalSize = sprintf(toSend, "NOK\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
			 }

		 }

		 else if (readyToSend == 3)
		 {
			 HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_SET);

			 if (diode == 1)
			 {
				 uint16_t finalSize = sprintf(toSend, "ON\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
			 }
			 else
			 {
				 uint16_t finalSize = sprintf(toSend, "OFF\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
			 }
		 }

		 else if (readyToSend == 4)
		 {

			 if(strcmp(binary_check, binary_pass) == 0)
			 {
				 uint16_t finalSize = sprintf(toSend, "YES\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
			 }
			 else
			 {
				 uint16_t finalSize = sprintf(toSend, "NO\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
			 }
		 }

		 else if (readyToSend == 5)
		 {
			 HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_RESET);
			 uint16_t finalSize = sprintf(toSend, "Diode off\r\n");
			 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
		 }
		 else if (readyToSend == 6)
		 {
			 if(volume == 1)
			 {
				 HAL_GPIO_WritePin(LED2_GPIO_Port, LED2_Pin, GPIO_PIN_SET);
				 uint16_t finalSize = sprintf(toSend, "OKK\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
				 volume = 0;
				 counter = 0;
			 }
			 else
			 {
				 HAL_GPIO_WritePin(LED2_GPIO_Port, LED2_Pin, GPIO_PIN_RESET);
				 uint16_t finalSize = sprintf(toSend, "NOT\r\n");
				 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
			 }
		 }

		 else if (readyToSend == 7) // command not found
		 {
			 uint16_t finalSize = sprintf(toSend, "unrecognized action\r\n");
			 HAL_UART_Transmit(&huart2, (uint8_t *)toSend, finalSize, 100);
		 }

		 readyToSend = 0;
	  }

  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE3);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 16;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 2;
  RCC_OscInitStruct.PLL.PLLR = 2;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */
void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim) {
    if (htim->Instance == TIM1) {
        if (HAL_GPIO_ReadPin(ECHO_GPIO_Port, ECHO_Pin) == GPIO_PIN_SET) {
            __HAL_TIM_SET_COUNTER(htim, 0); // Reset the counter
        } else {
            pulse_duration = __HAL_TIM_GET_COUNTER(htim);
            capture_done = 1;
        }
    }
}
/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
