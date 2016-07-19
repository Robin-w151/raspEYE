import raspEYE
import time
import datetime

from gpiozero import Button


def main():

    while True:

        button = Button(4)
        button.wait_for_press()

        fileName = 'image ' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '.png'

        raspEYE.takePicture(filename=fileName, sec=0, res=(2592, 1944))


if __name__ == '__main__':
    main()