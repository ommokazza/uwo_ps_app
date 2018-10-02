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

if __name__ == "__main__":
    estimator = ice.ImageCompareEstimator(ESTIMATOR_INPUTS)
    monitor = gsm.GameScreenMonitor(GAME_NAME)
    app = MainApp(estimator, FoxyFormatter(), monitor)
    app.mainloop()
