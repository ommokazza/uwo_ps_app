# UWO PS APP
UWO(Uncharted Waters Online) Price Share Aide.
This monitors the UWO screenshots and analyze them.
And then, generating a text to share the market rates.

# How to make executable file
1. Install [Anaconda3](https://www.anaconda.com/download/) - 'Add PATH'

2. Install [git-scm](https://git-scm.com/downloads)

3. Open 'Git CMD'

4. Make python 3.5 environment. pyinstaller has some problem in python 3.6.
<i>conda create -n py35 python=3.5.6 anaconda<br>
conda install -n py35 pip<br>
activate py35<br>
pip install -r requirements.txt</i>

5. Open a new 'Git CMD' on the project directory.<br>
<i>activate py35<br>
pyinstaller --noconsole --onefile --name "UWO Price Share Aide" main.py</i><br>