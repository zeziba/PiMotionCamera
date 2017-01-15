#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Python Motion Camera",
    version="0.5",
    description="This program uses the Raspberry Pi 2-3 camera and a PIR sensor to capture images."
                "Program was developed to be used by the Pueblo Community College for the pre-engineering"
                "students who use the Pi to develop skills with micro-controllers.",
    url="http://github.com/zeziba/IP_Checker",
    author="Charles Engen",
    platforms="Raspberry",
    author_email="owenengen@gmail.com",
    license="GNU GENERAL PUBLIC LICENSE V3",
    packages=['src', 'src.Capture', 'src.GUI', 'src.GUI.img_loader', 'src.Motion', 'src.PiCameraServer', ],
)
