from gpiozero import LED


class Flash:

    def __init__(self, gpio_pin):

        self.led = LED(3)

    def on(self):

        self.led.on()

    def off(self):

        self.led.off()