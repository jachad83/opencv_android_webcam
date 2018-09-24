import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# clear the frames folder
directory = 'frames'
if os.listdir(directory):
    for frame in os.listdir(directory):
        frame_path = os.path.join(directory, frame)
        os.unlink(frame_path)


# set the camera input
camera_input = cv2.VideoCapture(1)
frame_list =[]

def image_analysis(count):
    # iterate through frame captures
    for _ in range(count):
        frame_name = "frame_{}".format(_)
        input("Press Enter to capture frame.")
        print("{} captured.".format(frame_name))
        return_value, frame = camera_input.read()
        cv2.imwrite("frames/{}.png".format(frame_name), frame)
        frame_list.append("{}.png".format(frame_name))

    # load catured frames in greyscale
    for image in frame_list:
        img = cv2.imread('frames/{}'.format(image), 0)
        plt.imshow(img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])
        plt.show()
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=50,minRadius=100,maxRadius=200)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            print(image + " is a ball.")
            for i in circles[0, :]:
                # draw the outer circle
                cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
            cv2.imshow('detected circles', cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


# user sets number of frames to be analysed
frame_count = input('Enter how many frames to be analysed: ')
image_analysis(int(frame_count))
