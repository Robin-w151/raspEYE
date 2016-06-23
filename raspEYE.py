#!/usr/bin/env python3

import picamera
import time
import sys


def takePicture(filename, sec=1, res=(2592, 1944)):

    with picamera.PiCamera() as camera:

        camera.resolution = res
        camera.start_preview()
        
        # Camera warm-up time
        time.sleep(sec)
        camera.capture(filename)

if __name__ == "__main__":

    if "-c" in sys.argv:

        if "-f" in sys.argv:
            filename = sys.argv[sys.argv.index("-f") + 1]
        else:
            filename = "image.jpg"

        if "-r" in sys.argv:
            res = (int(sys.argv [sys.argv.index("-r") + 1]), int(sys.argv [sys.argv.index("-r") + 2]))
        else:
            res = (2592, 1944)

        if "-s" in sys.argv:
            sec = int(sys.argv[sys.argv.index("-s") + 1])
        else:
            sec = 1

        takePicture(filename, sec, res)
