"""
Created By: Charles Engen
10/6/2016
"""

import Capture.capture as capture
import Motion.motion as motion
import time
from picamera import PiCamera as Cam

# The following variables are used to determine how often the camera takes a picture when
# motion is detected.
# resolution can be much higher, play around with it till you are satisfied with results
# Must be a multiple of [32]x[16] in that format to correctly capture data
resolution = [480, 240]
interval = 1
# Read the PiCamera docs to see what file types can be used
# the PNG file type takes 32bits per pixel or 4 bytes, other types use varying amounts
# at 480x240 with 32bits per pixel the max size of the image is 3,686,400bits or 0.461MBs of data
# 480*240*32 = 3,686,400
file_type = ".png"

# Starts the camera
camera = Cam()

if __name__ == "__main__":
    try:
        while True:
            if motion.GPIO.event_detected(motion.INPIN):
                capture.capture_image(capture.file_location_generator(capture.generate_name()), camera, resolution)
                time.sleep(interval)
    except KeyboardInterrupt:
        camera.close()

