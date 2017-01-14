"""
Created By: Charles Engen
10/6/2016
"""

import getpass
import os
import random
import string
import time

import picamera

from src import config_parser

config = config_parser.ConfigSelectionMap(config_parser.configFile)


def capture_image(location, camera: picamera.PiCamera, type_=None)->bool:
    try:
        camera.capture(location, format=type_ if type_ is not None else location.split(".")[-1].lower())
        return True
    except picamera.PiCameraError as e:
        print("PiCamera Error: %s" % e)
        return False


def generate_name(string_size=4, override=(string.ascii_uppercase + string.digits),
                  ftype=config["Settings"]["format"])->str:
    a = time.strftime("%d_%m_%Y_")
    a += time.strftime("%H_%M_%S_")
    a += ''.join(random.SystemRandom().choice(override) for _ in range(string_size))
    a += ftype
    return a


def file_location_generator(file_name=generate_name(), override=config["Settings"]["save_location"])->str:
    override = os.path.join(override, "images", getpass.getuser())
    os.makedirs(override, exist_ok=True)
    return os.path.join(override, file_name)
