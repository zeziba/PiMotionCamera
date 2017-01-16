"""
Created By: Charles Engen
10/6/2016
Last Modification:
11/4/2016

Users can find more information on the PiCamera module at
    http://picamera.readthedocs.io/en/release-1.12/api_camera.html
"""

#  NEED TO TEST!!!

import Capture.capture as capture
import config_parser as config_get
import multiprocessing
from time import clock

from picamera import PiCamera as Cam

from Motion.motion import *

from GUI.main import MainFrame

from PiCameraServer.main import ConnectionManager

config = config_get.ConfigSelectionMap(config_get.configFile)

sleep_time = eval(config["Settings"]["interval"])

command_queue = multiprocessing.Queue()
event_queue = []


class CameraWorker(multiprocessing.Process):

    def __init__(self):
        super().__init__(self)
        self.commands = multiprocessing.Queue()
        global command_queue
        command_queue = self.commands
        self.camera = Cam(resolution=eval(config["Settings"]["resolution"]),
                          framerate=eval(config["Settings"]["framerate"]),
                          led_pin=eval(config["Settings"]["led_pin"]),
                          sensor_mode=eval(config["Settings"]["sensor_mode"]))

    def reconfig_camera(self):
        config_get.config_camera(self.camera, config)
        self.camera.close()
        global config
        config = config_get.ConfigSelectionMap(config_get.configFile)
        self.camera = Cam(resolution=eval(config["Settings"]["resolution"]),
                          framerate=eval(config["Settings"]["framerate"]),
                          led_pin=eval(config["Settings"]["led_pin"]),
                          sensor_mode=eval(config["Settings"]["sensor_mode"]))

    def capture(self):
        capture.capture_image(self.camera)

    def run(self):
        while True:
            data = self.commands.get()
            if data == 'shutdown':
                return
            if data == 'reconfig':
                self.reconfig_camera()
            if data == 'capture':
                self.capture()

    def terminate(self):
        global command_queue
        del command_queue
        self.commands.put("shutdown")
        super().terminate()


def add_event():
    command_queue.put('capture')
    print("Motion Captured")


if __name__ == "__main__":
    root = MainFrame()
    root.run()
    server = ConnectionManager()
    cam = CameraWorker()
    cam.start()

    last_pic = clock()

    try:
        while True:
            if GPIO.input(INPIN):
                if (clock() - last_pic).seconds > sleep_time:
                    cam.capture()
                    last_pic = clock()
    except KeyboardInterrupt as error:
        cam.terminate()
        root.quit()
