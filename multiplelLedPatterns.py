import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)

pins = [29, 31, 33, 35]

for pin in pins:
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, False)


def ledpattern(patterns, delay):
    for pattern in patterns:
        for p in pattern:
            for i in range(4):
                gpio.output(pins[i], int(p[i]))
        sleep(delay)


try:
    while True:
        p1 = ["1111"]
        p2 = ["1111"]
        p3 = ["1100", "0011", "1010", "0101"]

        ledpattern(p1, 0.1)
        ledpattern(p2, 0.1)
        ledpattern(p3, 0.1)

finally:
    gpio.cleanup()
