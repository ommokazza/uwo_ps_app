# UWO PS APP
UWO(Uncharted Waters Online) Price Share Aide.
This monitors the UWO screenshots and analyze them.
And then, generating a text to share the market rates.

# How to make executable file
1. Install Anaconda3 (https://www.anaconda.com/download/)

2. Make python 3.5 environment. pyinstaller has some problem in python 3.6  
  conda install python=3.5.6  
  conda create -n py35 python=3.5.6 anaconda  
  conda install -n py35 pip  
  activate py35  
  pip install tensorflow  
  pip install pillow  
  pip install watchdog  
  pip install pandas  
  pip install imgurpython  
  pip install pyinstaller  
  pip install --upgrade git+https://github.com/ommokazza/uwo_ps_utils.git@master#egg=uwo_ps_utils  

3. Open a new cmd window  
  activate py35  
  pyinstaller --noconsole --onefile --name "UWO Price Share Aide" main.py
