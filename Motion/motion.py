"""
Created By: Charles Engen
10/6/2016
"""

import functools
from RPi import GPIO
# Comment out following line when moved to RPi
GPIO.VERBOSE = False

INPIN = 11 # Signal in
OUTPIN = 3 # LED

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPIN, GPIO.IN)
GPIO.setup(OUTPIN, GPIO.OUT)


def check_movement()->bool:
    t = GPIO.output(INPIN)
    GPIO.input(OUTPIN, t)
    return t

