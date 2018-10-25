# UWO PS APP
UWO(Uncharted Waters Online) Price Share Aide.
This monitors the UWO screenshots and analyze them.
And then, generating a text to share the market rates.

# How to make executable file
1. Install [Anaconda3](https://www.anaconda.com/download/) - 'Add PATH'

2. Install [git-scm](https://git-scm.com/downloads)

3. Open 'Git CMD'

4. Make python 3.5 environment. pyinstaller has some problem in python 3.6.<br>
<i>(For 32-bit environment on 64-bit windows, 'set CONDA_FORCE_32BIT=1')<br>
conda create -n py35 python=3.5.6 anaconda<br>
conda install -n py35 pip<br>
activate py35<br>
pip install --upgrade -r requirements.txt</i>

5. Open a new 'Git CMD' on the project directory.<br>
<i>(For 32-bit environment on 64-bit windows, 'set CONDA_FORCE_32BIT=1')<br>
activate py35<br>
pyinstaller --noconsole --onefile --name "UWO Price Share Aide" main.py</i><br>

6. Bundle 'resources' directory and 'NanumGothic.ttf' file with .exe
