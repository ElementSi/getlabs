from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2560, 1440)
camera.rotation = 180

def take_photo(name):
    camera.start_preview()
    sleep(5)
    camera.capture("/home/gr106/Desktop/lab3/light-main/data/" + name +".png")
    camera.stop_preview()

take_photo()
