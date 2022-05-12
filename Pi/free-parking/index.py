# Natthawee Koengfak 6213125
# https://docs.google.com/spreadsheets/d/1-Hp5QSB9J4o3Ljcb1Mn9XatZvVPePCXGoufBd5jaR5k/edit?usp=sharing
import time
from datetime import datetime


import RPi.GPIO as GPIO


from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment


# Initialize Netpie information
NETPIE_HOST = "broker.netpie.io"
CLIENT_ID = "9c389ca8-6e95-4063-916d-52f284b5684d"  # YOUR CLIENT ID
DEVICE_TOKEN = "tYEw2842zc1iWR6zHHMhcrtpeTYaaCN2"  # YOUR TOKEN


# gpio init
def gpio_init(outp=[], inp=[]):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    for i in outp:
        GPIO.setup(i, GPIO.OUT)
    for i in inp:
        GPIO.setup(i, GPIO.IN)


# connect ggs
def connect(SheetName, GSheet_OAUTH_JSON, worksheet_name, scope):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        GSheet_OAUTH_JSON, scope)
    client = gspread.authorize(credentials)
    worksheet = client.open(SheetName).worksheet(worksheet_name)
    return worksheet


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
            print([GPIO.input(e) for e in self.ir])
            time.sleep(1)


if __name__ == "__main__":
    main()
