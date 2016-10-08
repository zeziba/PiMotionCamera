"""
Created By: Charles Engen
10/6/2016
"""

import picamera
import os
import string
import random


def capture_image(location, camera: picamera.PiCamera, res: list, _type=None)->bool:
    try:
        try:
            os.mkdir(os.path.split(location)[0])
        except Exception:
            pass
        camera.resolution = (res[0], res[1])
        camera.capture(location, format=_type)
        return True
    except picamera.PiCameraError:
        return False


def generate_name(string_size=12, override=(string.ascii_uppercase + string.digits))->str:
    a = ''.join(random.SystemRandom().choice(override) for _ in range(string_size))
    a += ".jpg"
    return a


def file_location_generator(file_name=generate_name(), override=os.getcwd())->str:
    return os.path.join(override, "images", file_name)
