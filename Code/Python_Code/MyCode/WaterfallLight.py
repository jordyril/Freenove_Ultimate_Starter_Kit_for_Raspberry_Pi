import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]  # BOARD
sleeping_time = 0.5


def setup():
    GPIO.setmode(GPIO.BOARD)  # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT)  # set all ledPins to OUTPUT mode
    GPIO.output(
        ledPins, GPIO.LOW
    )  # make all ledPins output HIGH level, turn off all led


def loop():
    while True:
        for pin in ledPins:  # make led(on) move from left to right
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(sleeping_time)
            GPIO.output(pin, GPIO.LOW)
        for pin in ledPins[::-1]:  # make led(on) move from right to left
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(sleeping_time)
            GPIO.output(pin, GPIO.LOW)


def destroy():
    GPIO.cleanup()  # Release all GPIO


if __name__ == "__main__":  # Program entrance
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
