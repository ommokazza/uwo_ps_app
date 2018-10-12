import configparser
import os
from pathlib import Path

from src.uwo_ps_app.gui import MainApp
from src.uwo_ps_app import image_comapre_estimator as ice
from src.uwo_ps_app.formatter import FoxyFormatter
from src.uwo_ps_app import game_screen_monitor as gsm


ESTIMATOR_INPUTS = [
    ("./resources/goods.png", "./resources/goods.labels"),
    ("./resources/towns.png", "./resources/towns.labels"),
    ("./resources/rates.png", "./resources/rates.labels"),
    ("./resources/arrows.png", "./resources/arrows.labels")
]

GAME_NAME = "Uncharted Waters Online"
CONFIG_FILE = "config.ini"
config = configparser.ConfigParser()

DEFAULT = 'Default'
KEY_INTERVAL = 'interval'

def __load_config():
    config.read(CONFIG_FILE)
    try:
        config[DEFAULT]
    except KeyError:
        config[DEFAULT] = {}

def __save_config():
    try:
        f = open(CONFIG_FILE, "w")
        config.write(f)
    except:
        print("Something wrong while writing config")

if __name__ == "__main__":
    __load_config()

    estimator = ice.ImageCompareEstimator(ESTIMATOR_INPUTS)
    monitor = gsm.GameScreenMonitor(GAME_NAME)
    try:
        monitor.set_interval(float(config[DEFAULT][KEY_INTERVAL]))
    except KeyError:
        print("No interval config")

    app = MainApp(estimator, FoxyFormatter(), monitor)
    app.mainloop()

    config[DEFAULT][KEY_INTERVAL] = str(monitor.get_interval())
    __save_config()
    
