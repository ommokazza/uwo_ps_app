import os
from pathlib import Path

from src.uwo_ps_app.gui import MainApp
from src.uwo_ps_app.estimator import TensorFlowEstimator
from src.uwo_ps_app.formatter import FoxyFormatter
from src.uwo_ps_app.screenshot_monitor import DirectoryMonitor


MODEL_DIRS = [
    "./resources/model_goods",
    "./resources/model_towns",
    "./resources/model_rates",
    "./resources/model_arrows"]
LABEL_PATHS = [
    "./resources/goods.labels",
    "./resources/towns.labels",
    "./resources/rates.labels",
    "./resources/arrows.labels"]

SCREENSHOT_DIR = os.path.join(str(Path.home()),
                              'Documents', 'KOEI',
                              'GV Online Eg', 'ScreenShot')

if __name__ == "__main__":
    estimator = TensorFlowEstimator(MODEL_DIRS, LABEL_PATHS)
    monitor = DirectoryMonitor(SCREENSHOT_DIR)
    app = MainApp(estimator, FoxyFormatter(), monitor)
    app.mainloop()
