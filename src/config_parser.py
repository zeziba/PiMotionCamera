"""
Created By: Charles Engen
11/4/2016
Last Modification:
11/4/2016

This module creates a config.ini file to use for the PiCamera, it sets many default params. If any are changed ensure
the program is restarted to see the effects. Also ensure that if a value is changed in this program you understand
what it will do. If the config.ini file is corrupted or modified and no longer works, delete the file and run this
program again.
"""

import os
from os.path import join
import configparser

configFile = "config.ini"
defaultConfig = {"Settings": {
        "resolution": [3280, 2464],
        "format": ".PNG",
        "interval": 1.000,
        "sharpness": 0,
        "contrast": 0,
        "saturation": 0,
        "brightness": 50,
        "iso": 800,
        "video_stabilization": False,
        "exposure_compensation": 0,
        "exposure_mode": "auto",
        "meter_mode": "average",
        "awb_mode": "auto",
        "image_effect": "none",
        "color_effects": None,
        "rotation": 0,
        "hflip": True,
        "vflip": False,
        "crop": (0.0, 0.0, 1.0, 1.0),
        "framerate": 15,
        "sensor_mode": 0,
        "led_pin": 3,
        "quality": 100,
        "PIR": 16,
        "warnings": False,
        "save_location": join("/", "mnt", "smbServer")
    }
}

try:
    with open(join(os.getcwd(), "%s" % configFile), "r") as f:
        pass
except Exception as error:
    with open(join(os.getcwd(), "%s" % configFile), "w+") as f:
        tempConf = configparser.ConfigParser()
        for header in defaultConfig.keys():
            tempConf.add_section("%s" % header)
            for option in defaultConfig[header].keys():
                tempConf.set(header, option, str(defaultConfig[header][option]))
        tempConf.write(f)
finally:
    config = configparser.ConfigParser()
    config.read(configFile)


def ConfigSelectionMap(file, section=None):
    dict1 = {}
    if section is not None:
        options = file.options(section)
        for option in options:
            try:
                dict1[option] = file.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except Exception as r:
                print("Exception on %s\n%s" % (option, r))
    else:
        for section_ in config:
            if section_ != "DEFAULT":
                dict1[section_] = dict()
                for option in config.options(section_):
                    dict1[section_][option] = config[section_][option]
    return dict1


def config_camera(camera, cnf: dict()):
    camera.sharpness = eval(cnf["Settings"]["sharpness"])
    camera.contrast = eval(cnf["Settings"]["contrast"])
    camera.brightness = eval(cnf["Settings"]["brightness"])
    camera.saturation = eval(cnf["Settings"]["saturation"])
    camera.ISO = eval(cnf["Settings"]["iso"])
    camera.video_stabilization = eval(cnf["Settings"]["video_stabilization"])
    camera.exposure_compensation = eval(cnf["Settings"]["exposure_compensation"])
    camera.exposure_mode = cnf["Settings"]["exposure_mode"]
    camera.meter_mode = cnf["Settings"]["meter_mode"]
    camera.awb_mode = cnf["Settings"]["awb_mode"]
    camera.image_effect = cnf["Settings"]["image_effect"]
    camera.color_effects = eval(cnf["Settings"]["color_effects"])
    camera.rotation = eval(cnf["Settings"]["rotation"])
    camera.hflip = eval(cnf["Settings"]["hflip"])
    camera.vflip = eval(cnf["Settings"]["vflip"])
    camera.crop = eval(cnf["Settings"]["crop"])


if __name__ == "__main__":
    print(ConfigSelectionMap(config))
