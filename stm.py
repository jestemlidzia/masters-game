import serial
import serial.tools.list_ports


class STM(object):
    def __init__(self):
        self.ports_list = []
        self.value = 0
        print('start')

    def find_port(self):
        ports = serial.tools.list_ports.comports()
        print(ports)
        for device in ports:
            self.ports_list.append(device.name)
            print(device.name)
            # self.port_box.addItems([str(device)])

    def board_connection(self):
        print('Select com port and baud rate: COM3, 115200')
        try:
            self.ser = serial.Serial(port='COM3', baudrate=115200, timeout=None)
            # self.ser = serial.Serial("COM3", "115200", timeout=None)
            print('weszlo')
            return 1
        except Exception as exc:
            print(f"Exception: {exc}")
            return 0

    def write_sth(self, info):
        send_info = info + "\n"
        self.ser.write(send_info.encode())
        try:
            data = self.ser.readline()
            dec_data = str(data.decode('utf-8'))
            self.value = dec_data
            print('value from stm: ', self.value)
        except Exception as exc:
                print(f"Exception: {exc}")

    def read_sth(self):
        try:
            read_data = self.ser.readline()
            dec_read_data = str(read_data.decode('utf-8'))
            self.read_value = dec_read_data
            print('message from stm: ', self.read_value)
        except Exception as exc:
                print(f"Exception: {exc}")


    def updd(self):
        self.find_port()
        if self.board_connection():
            self.write_sth()


# gee = STM()
# gee.updd()