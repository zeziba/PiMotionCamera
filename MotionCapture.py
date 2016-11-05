"""
Created By: Charles Engen
10/6/2016
Last Modification:
11/4/2016

Users can find more information on the PiCamera module at
    http://picamera.readthedocs.io/en/release-1.12/api_camera.html
"""

import Capture.capture as capture
import Motion.motion as motion
import time
from picamera import PiCamera as Cam
import config_parser as configGet


config = configGet.ConfigSelectionMap(configGet.configFile)

# Starts the camera with settings from the config.ini file
# The config_parser.py must be run at least once to generate the file, will be done automatically
# when this file is run.
camera = Cam(resolution=eval(config["Settings"]["resolution"]), framerate=eval(config["Settings"]["framerate"]),
             led_pin=eval(config["Settings"]["led_pin"]), sensor_mode=eval(config["Settings"]["sensor_mode"]))

configGet.config_camera(camera, config)


if __name__ == "__main__":
    try:
        while True:
            if motion.GPIO.event_detected(motion.INPIN):
                capture.capture_image(capture.file_location_generator(capture.generate_name()), camera)
                time.sleep(eval(config["Settings"]["interval"]))
    except KeyboardInterrupt:
        camera.close()

