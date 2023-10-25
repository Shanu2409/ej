import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
LedPin = 14
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, False)
try:
    while True:
        GPIO.output(LedPin, True)
        print("LED ON")
        sleep(1)
        GPIO.output(LedPin, False)
        print("LED OFF")
        sleep(1)

finally:
    GPIO.output(LedPin, False)
    GPIO.cleanup()
