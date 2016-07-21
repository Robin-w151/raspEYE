#!/usr/bin/env python3

import flash
import raspEYE
import time
import datetime

from gpiozero import Button


def main():

    FLASH = flash.Flash(3)
    BUTTON = Button(14)

    while True:

        BUTTON.wait_for_press()

        print('Capturing...')

        fileName = 'image ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '.png'

        FLASH.on()

        raspEYE.takePicture(fileName, sec=0, res=(1000, 750))

        FLASH.off()

        print('Finished')


if __name__ == '__main__':
    main()
