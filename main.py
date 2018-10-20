import cv2
import os
import sys
import numpy as np
from matplotlib import pyplot as plt

# clear the frames folder
DIRECTORY = "frames"

if os.listdir(DIRECTORY):
    for frame in os.listdir(DIRECTORY):
        _frame_path = os.path.join(DIRECTORY, frame)
        os.unlink(_frame_path)


def image_analysis(count):
    # set the camera input
    _camera_output = cv2.VideoCapture(0)
    _frame_list = []

    # iterate through frame captures
    for _ in range(count):
        _frame_name = "frame_{}".format(_)
        input("Press Enter to capture frame.")
        print("{} captured.".format(_frame_name))
        return_value, frame = _camera_output.read()
        # name and write the frames to images
        cv2.imwrite(DIRECTORY + "/{}.png".format(_frame_name), frame)
        _frame_list.append("{}.png".format(_frame_name))

    # load captured frames in greyscale
    for image in _frame_list:
        # use Circle Hough Transform to find circles
        _img = cv2.imread(DIRECTORY + "/{}".format(image), 0)
        _circles = cv2.HoughCircles(_img, cv2.HOUGH_GRADIENT, 1, 20,
                                    param1=50, param2=50, minRadius=100, maxRadius=200)
        # display the images for debugging purposes
        plt.imshow(_img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])
        plt.show()

        # select image if a circle is found
        if type(_circles) is np.ndarray:
            print(image + " is a ball.")
            # display the circles for debugging purposes
            _circles = np.uint16(np.around(_circles))
            cimg = cv2.cvtColor(_img, cv2.COLOR_GRAY2BGR)
            for i in _circles[0, :]:
                cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        else:
            print(image + " is NOT a ball.")

    sys.exit(0)


def main():
    # user sets number of frames to be analysed
    frame_count = input('Enter how many frames to be analysed: ')
    image_analysis(int(frame_count))


if __name__ == "__main__":
    main()
