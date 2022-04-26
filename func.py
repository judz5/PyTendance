from picamera import PiCamera
from time import sleep
import cv2, face_recognition, os
import numpy as np

camera = piCamera()

# Take photo func, name will be passed in from gui, not sure how yet
def takePhoto():
    name = "temp" # temp var
    camera.capture('/Studentimage/%s.jpg' % name) # take photo and save



