import time
import serial
import RPi.GPIO as GPIO

# Set up gpio for button push
PIN_NUM = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN_NUM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


class HardwareInterface:

    def __init__(self):
        # Set up printer
        self.ser = serial.Serial('/dev/serial0', 19200)

        # To write to serial port do:
        # ser.write(b'Your text here\n\n')

    def isButtonPressed(self) -> bool:
        return GPIO.input(PIN_NUM) == GPIO.HIGH
    
    def writeToPrinter(self, st: str):
        self.ser.write(st.encode())

if __name__ == '__main__':
    print("hardware_interface.py")
