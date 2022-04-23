import RPi.GPIO as GPIO
from time import sleep

ledpin = 13
buttonpin = 23


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledpin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(buttonpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    while True:
        # GPIO.output(ledpin, GPIO.HIGH)
        # sleep(3)
        # GPIO.output(ledpin, GPIO.LOW)
        # sleep(2)

        # print(GPIO.input(buttonpin))
        # sleep(0.1)

        if GPIO.input(buttonpin) == 0:
            GPIO.output(ledpin, GPIO.HIGH)
        else:
            GPIO.output(ledpin, GPIO.LOW)


def clean_up():
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        clean_up()
        print("program ended")
