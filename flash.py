
import time

from gpiozero import LED


class Flash(LED):

    def __init__(self, gpio_pin):
        LED.__init__(self, gpio_pin)

    def timer(self, seconds):

        self.on()

        time.sleep(seconds)

        self.off()
