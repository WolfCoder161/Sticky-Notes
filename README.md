# Sticky Notes
## Description
Thank you for using Sticky Notes. Sticky Notes is a program that allows you to mimic regular desk sticky notes on your PC. Sticky Notes was designed to be simple so you can use with no distractions. Sticky Notes currently can open and allow direct editing to any existing .txt file. Sticky Notes saves your notes in the .txt format so you can edit and view them at your convenience.
## Installation
To use Sticky Notes, you need to have python installed. Additionally, Sticky Notes depends on the PySimpleGui and subprocess python libraries.
### Install
 1. Clone or download and unzip the main branch
 2. Navigate to the directory in a terminal (or CMD) `cd Sticky-Notes`
 3. Install all python prerequisites `python -m pip install -r requirements.txt`
## Usage
To use this program, just run `python main.py`
## Executable
Use the python PyInstaller module to create a executable. Check its [documentation ](https://pyinstaller.readthedocs.io/en/stable/) for more details on how to use it.
To create an executable of Sticky Notes, you will first need to edit the function name on line 94 to `createNewInstanceExe()` instead of `createNewInstance()`. Once you have done that and after you have installed PyInstaller, run `python -m PyInstaller --noconsole --onefile --icon=.\optional-resources\stickyNotes.ico ./main.py`
## License
This projects is licensed under the GNU General Public License v3.0. Click [here](LICENSE) to view the license text.

