import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Looking for Cards")
print("Press Crtl+c to stop")

try:
    text = input("Enter New Data: ")
    print("Now place your tag to write......")
    reader.write(text)
    print(" Data Writeen")
finally:
    GPIO.cleanup()
