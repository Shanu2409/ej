from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()
sleep(2)
camera.capture("/home/pi/Pictures/newImage.jpg")
camera.stop_preview()
