# Natthawee Koengfak 6213125
import time
from datetime import datetime


import RPi.GPIO as GPIO


from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment


# gpio init
def gpio_init(outp=[], inp=[]):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    for i in outp:
        GPIO.setup(i, GPIO.OUT)
    for i in inp:
        GPIO.setup(i, GPIO.IN)


def toggle(pin, condition=False):
    GPIO.output(pin, GPIO.HIGH if condition else GPIO.LOW)


def main():
    main_class = Main()
    main_class.run()


class Main:
    # led
    ir = [32, 36, 38, 40]
    led = [31, 33, 35, 37]

    def __init__(self):
        # using gpio
        gpio_init(outp=self.led, inp=self.ir)

        # 7seg
        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=1)
        self.seg = sevensegment(self.device)

    def run(self):
        while True:
            sum = 0
            for i, e in enumerate(self.ir):
                toggle(self.led[i], GPIO.input(e))
                sum += GPIO.input(e)

            self.seg.text = str(sum)
            time.sleep(1)


if __name__ == "__main__":
    main()
