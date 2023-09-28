#include "main.h"
#include "usart.h"
#include "gpio.h"

char *read_keyboard(void)
{

	HAL_GPIO_WritePin(R1_GPIO_Port, R1_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(R2_GPIO_Port, R2_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R3_GPIO_Port, R3_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R4_GPIO_Port, R4_Pin, GPIO_PIN_SET);


	if(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "1";
	}

	if(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "2";
	}

	if(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "3";
	}

	if(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "A";
	}

	HAL_GPIO_WritePin(R1_GPIO_Port, R1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R2_GPIO_Port, R2_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(R3_GPIO_Port, R3_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R4_GPIO_Port, R4_Pin, GPIO_PIN_SET);


	if(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "4";
	}

	if(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "5";
	}

	if(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "6";
	}

	if(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "B";
	}

	HAL_GPIO_WritePin(R1_GPIO_Port, R1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R2_GPIO_Port, R2_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R3_GPIO_Port, R3_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(R4_GPIO_Port, R4_Pin, GPIO_PIN_SET);


	if(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "7";
	}

	if(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "8";
	}

	if(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "9";
	}

	if(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "C";
	}

	HAL_GPIO_WritePin(R1_GPIO_Port, R1_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R2_GPIO_Port, R2_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R3_GPIO_Port, R3_Pin, GPIO_PIN_SET);
	HAL_GPIO_WritePin(R4_GPIO_Port, R4_Pin, GPIO_PIN_RESET);


	if(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C1_GPIO_Port, C1_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "*";
	}

	if(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C2_GPIO_Port, C2_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "0";
	}

	if(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C3_GPIO_Port, C3_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "#";
	}

	if(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)))
	{
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_SET);
		while(!(HAL_GPIO_ReadPin(C4_GPIO_Port, C4_Pin)));
		HAL_GPIO_WritePin(LD2_GPIO_Port, LD2_Pin, GPIO_PIN_RESET);
		return "D";
	}

}

char *read_result(void)
{
	int i = 0;
	char result[5];
	while(i<5)
	{
		result[i] = read_keyboard();
	}
}

