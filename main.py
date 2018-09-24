import cv2
import numpy as np
from matplotlib import pyplot as plot
import os, shutil


directory = 'frames'
if os.listdir(directory):
    print(os.listdir(directory))
    for frame in os.listdir(directory):
        frame_path = os.path.join(directory, frame)
        os.unlink(frame_path)


camera_input = cv2.VideoCapture(1)


def image_analysis(count):
    for _ in range(count):
        input("Press Enter to capture frame.")
        print("Frame {} captured".format(_))
        return_value, frame = camera_input.read()
        cv2.imwrite("frames/frame_{}.png".format(_), frame)


frame_count = input('Enter how many frames to be analysed: ')
image_analysis(int(frame_count))
