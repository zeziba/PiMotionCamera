"""
Created By: Charles Engen
10/6/2016
"""

import picamera
import os
import time
import string
import random
import config_parser
import getpass

config = config_parser.ConfigSelectionMap(config_parser.configFile)


def capture_image(location, camera: picamera.PiCamera, type_=None)->bool:
    try:
        ta = os.path.split(location)
        tb = ""
        try:
            for loc in ta:
                tb = os.path.join(tb, loc)
                try:
                    os.mkdir(tb)
                except Exception as er:
                    pass
        except Exception:
            pass
        camera.capture(location, format=type_ if type_ is not None else location.split(".")[-1])
        return True
    except picamera.PiCameraError:
        return False


def generate_name(string_size=4, override=(string.ascii_uppercase + string.digits),
                  ftype=config["Settings"]["format"])->str:
    a = time.strftime("%d_%m_%Y_")
    a += time.strftime("%H_%M_%S_")
    a += ''.join(random.SystemRandom().choice(override) for _ in range(string_size))
    a += ftype
    return a


def file_location_generator(file_name=generate_name(), override=config["Settings"]["save_location"])->str:
    return os.path.join(override, "images", getpass.getuser(), file_name)
