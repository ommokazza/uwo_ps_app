import tkinter as tk
from tkinter.filedialog import askdirectory

from datetime import datetime
from pathlib import Path
import pandas as pd
import webbrowser

from monitor import DirectoryMonitor
from estimator import TensorFlowEstimator
from formatter import FoxyFormatter

class MainApp(tk.Tk):
    PAD = "7"
    screenshot_dir = str(Path.home())\
                   + '\\Documents\\KOEI\\GV Online Eg\\ScreenShot'

    def __init__(self, estimator, formatter):
        tk.Tk.__init__(self)
        self.estimator = estimator
        self.formatter = formatter

        self.title("UWO Price Share Aide")
        self.geometry("640x240")

        self.__create_menus()
        self.__create_ui()

        self.monitor = DirectoryMonitor(self.on_screenshot_added)
        self.monitor.set_path(self.screenshot_dir)

    def __create_menus(self):
        self.menubar = tk.Menu(self, tearoff=0, relief="raised")
        self.menubar.add("command", label="About", 
                         command=self.menu_about, underline=0)
        self.menubar.add("separator")
        self.menubar.add("command", label="Select Directory",
                         command=self.menu_select_directory, underline=0)
        self.menubar.add("separator")
        self.menubar.add("command", label="Report Screenshot",
                         command=self.menu_report_screenshot, underline=0)
        self.config(menu=self.menubar)
    
    def __create_ui(self):
        result_frame = tk.Frame(self, relief="flat", bd=1)
        result_frame.pack(side="top", 
                          fill="x", expand=False)

        self.result_str = tk.StringVar()
        self.result_view = tk.Entry(result_frame,
                                    textvariable=self.result_str)
        self.result_view.pack(side="left", anchor="w",
                              padx=self.PAD, pady=self.PAD,
                              fill="x", expand=True)

        self.copy_btn = tk.Button(result_frame, text="Copy To Clipboard")
        self.copy_btn.pack(side="right", anchor="w",
                           padx=self.PAD, pady=self.PAD)
        self.copy_btn.bind("<Button-1>", self.copy_to_clipboard)

        self.list_frame = tk.LabelFrame(self, text=" History ")
        self.list_frame.pack(side="bottom", anchor="n",
                             padx=self.PAD, pady="3",
                             fill="both", expand=True)
        self.list_box = tk.Listbox(self.list_frame, highlightthickness=0,
                                   bd=0, activestyle="none")
        self.list_box.pack(side="top", anchor="n",
                           padx="0", pady="0",
                           fill="both", expand=True)

    def on_screenshot_added(self, path):
        result = self.estimator.estimate(path)
        if not result:
            return

        self.result_str.set(self.formatter.apply(result))
        self.copy_to_clipboard(None)

        list_item = '(' + datetime.now().strftime('%H:%M') + ') '\
                  + self.result_str.get()
        self.list_box.insert(0, list_item)
        self.list_box.see(0)
        self.attributes('-topmost', 1)
        self.attributes('-topmost', 0)

    def menu_about(self):
        webbrowser.open('https://github.com/ommokazza/uwo_ps_app')

    def menu_select_directory(self):
        selected_dir = askdirectory(initialdir=self.screenshot_dir)
        if selected_dir:
            self.screenshot_dir = selected_dir
            self.monitor.set_path(self.screenshot_dir)

    def menu_report_screenshot(self):
        pass#TODO

    def copy_to_clipboard(self, event):
        df = pd.DataFrame([self.result_str.get()])
        df.to_clipboard(index=False,header=False)


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

if __name__ == "__main__":
    estimator = TensorFlowEstimator(MODEL_DIRS, LABEL_PATHS)
    app = MainApp(estimator, FoxyFormatter())
    app.mainloop()