# MIT License
# Copyright (c) 2019 JetsonHacks
# See license
# Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
# NVIDIA Jetson Nano Developer Kit using OpenCV
# Drivers for the camera and OpenCV are included in the base image

import cv2
#import time

# gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
# Defaults to 1280x720 @ 60fps
# Flip the image by setting the flip_method (most common values: 0 and 2)
# display_width and display_height determine the size of the window on the screen


def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink" % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        ))


width = 1280
height = 720
zoom = 0.5
delay = 0.5


def write_image():
    #count = 0
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    pipline = gstreamer_pipeline(flip_method=0,
                                 framerate=10,
                                 capture_width=width,
                                 capture_height=height,
                                 display_width=width,
                                 display_height=height)
    cap = cv2.VideoCapture(pipline, cv2.CAP_GSTREAMER)

    while cap.isOpened():
        ret_val, img = cap.read()
        if (ret_val):
            cv2.imwrite("cur_pic.bmp", img)
            #img = cv2.resize(img, (0,0), fx=zoom, fy=zoom)
            #cv2.imshow("test", img)
            #count += 10 # i.e. at 30 fps, this advances one second
            #cap.set(cv2.CAP_PROP_POS_FRAMES, count)
            #time.sleep(delay)
        else:
            cap.release()
            cv2.destroyAllWindows()
            exit()

        # This also acts as
        keyCode = cv2.waitKey(30) & 0xFF
        # Stop the program on the ESC key
        if keyCode == 27 or not ret_val:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    write_image()