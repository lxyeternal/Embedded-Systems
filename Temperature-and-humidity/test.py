import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

i = 0
try:
    while True:

        if i > 100:

            break
        GPIO.output(11, True)
        time.sleep(0.5)
        GPIO.output(11, False)
        time.sleep(0.5)
        i += 1

finally:
    GPIO.cleanup()

