# import
# import RPi.GPIO as GPIO
import time

# define slot pins
slot = [31, 33, 35, 37]
# define output
output = []
# define previous state
prev = {}


# contain
# gpio board
# gpio set i/o pin
def init():
    # GPIO.setmode(GPIO.BOARD)
    for i in slot:
        # GPIO.setup(i, GPIO.IN)
        prev[i] = False
    for i in output:
        # GPIO.setup(i, GPIO.OUT)
        pass


# fucntion that check prev state != current state

def is_car_in():
    pass


def is_car_out():
    pass


# main
def main():
    init()
    print("Hello World")
    while True:
        # get notification
        # loop through notifications
        # process notification

        # loop through slots
        for pos in prev:
            # cheking if slot is true mean car is in slot
            # if(GPIO.input(i)):
            #     pass
            print(pos, prev[pos])
        time.sleep(5)


if __name__ == "__main__":
    main()
