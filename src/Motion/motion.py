"""
Created By: Charles Engen
10/6/2016
"""

from RPi import GPIO

from src import config_parser

config = config_parser.ConfigSelectionMap(config_parser.configFile)

# Comment out following line when moved to RPi
GPIO.VERBOSE = False

INPIN = eval(config["Settings"]["pir"])  # Signal in
OUTPIN = eval(config["Settings"]["led_pin"])  # LED

GPIO.setwarnings(eval(config["Settings"]["warnings"]))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPIN, GPIO.IN)
GPIO.setup(OUTPIN, GPIO.OUT)

GPIO.add_event_detect(INPIN, GPIO.RISING)

