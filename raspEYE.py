#!/usr/bin/env python3

import io
import picamera
import sys
import time

from gpiozero import LED
from PIL import Image


class Flash:

    def __init__(self, gpio_pin):

        self.led = LED(3)

    def on(self):

        self.led.on()

    def off(self):

        self.led.off()


def takePicture(filename="image.png", sec=1, res=(2592, 1944), bw=True, use_flash=True):

    with picamera.PiCamera() as camera:

        stream = io.BytesIO()

        camera.resolution = res
        camera.start_preview()

        # Turn flash on
        flash = Flash(gpio_pin=3)
        if use_flash:
            print('Flash on')
            flash.on()

        # Camera warm-up time
        time.sleep(sec)
        camera.capture(stream, format='png')

        # Turn flash off
        if use_flash:
            print('Flash off')
            flash.off()

        stream.seek(0)
        image = Image.open(stream)

        if bw:
            image = image.convert('LA')

        image.save(filename)

if __name__ == "__main__":

    if "-c" in sys.argv:

        if "-f" in sys.argv:
            filename = sys.argv[sys.argv.index("-f") + 1]
        else:
            filename = "image.png"

        if "-r" in sys.argv:
            res = (int(sys.argv [sys.argv.index("-r") + 1]), int(sys.argv [sys.argv.index("-r") + 2]))
        else:
            res = (2592, 1944)

        if "-s" in sys.argv:
            sec = int(sys.argv[sys.argv.index("-s") + 1])
        else:
            sec = 1

        takePicture(filename, sec, res)
