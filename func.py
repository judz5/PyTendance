from picamera import PiCamera
from time import sleep
import cv2, face_recognition, os
import numpy as np
import pandas as pd
import gui_manager

camera = piCamera()

# Take photo func, name will be passed in from gui, not sure how yet
def takePhoto():
    name = "temp" # temp var
    camera.capture('/Studentimage/%s.jpg' % get_name()) # take photo and save



