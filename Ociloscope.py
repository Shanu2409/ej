import time
import matplotlib.pyplot as plt
from drawnow import *
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = []

plt.ion()
adc.start_adc(0, gain=GAIN)


def makeFig():
    plt.ylim(-5000, 5000)
    plt.title("Oscilloscope")
    plt.grid(True)
    plt.ylabel("ADC outputs")
    plt.plot(val, "ro-", label="Channel 0")
    plt.legend(loc="lower right")


while True:
    value = adc.get_last_result()
    print(f"Channel 0: {value}")
    time.sleep(0.5)
    val.append(int(value))
    drawnow(makeFig)
    plt.pause(0.000001)
    if len(val) > 50:
        val.pop(0)
