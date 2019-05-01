import RPi.GPIO as GPIO
import threading

class PiController:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.led_pin = 17
        self.mortar_pin = 18

        self.gpio = GPIO
        self.gpio.setmode(GPIO.BCM)
        self.gpio.setup(self.led_pin, GPIO.OUT)
        self.gpio.setup(self.mortar_pin, GPIO.OUT)
        print('-- GPIO initialized! --')

    # @TODO The cleaning up is not working...
    def __del__(self):
        self.gpio.cleanup()

    # @TODO The cleaning up is not working...
    def cleanup(self):
        self.gpio.cleanup()

    def led_on(self):
        self.gpio.output(self.led_pin, True)

    def led_off(self):
        self.gpio.output(self.led_pin, False)

    def mortar_on(self):
        self.gpio.output(self.mortar_pin, True)

    def mortar_off(self):
        self.gpio.output(self.mortar_pin, False)

