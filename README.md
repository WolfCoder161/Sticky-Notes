![Logo](https://user-images.githubusercontent.com/69877833/132152001-f103d838-931e-4041-a3e9-7412688c8dec.png)

# Sticky Notes
[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
## Description
Thank you for using Sticky Notes. Sticky Notes is a program that allows you to mimic regular desk sticky notes on your PC. Sticky Notes was designed to be simple so you can focus with no distractions. Sticky Notes currently can open and allow direct editing to any existing .txt file. Sticky Notes saves your notes in .txt format so you can edit and view them in other text editors at your convenience. Sticky Notes works on all major platforms that support Python3 (E.g. Linux, macOS, Windows, etc.).
## Installation
To use Sticky Notes, you need to have python installed. Additionally, Sticky Notes depends on the PySimpleGui and subprocess python libraries.
### Install
 1. Clone or download and unzip the main branch
 2. Navigate to the directory in a terminal (E.g. CMD, Linux terminal, etc.) `cd Sticky-Notes`
 3. Install all python prerequisites `python -m pip install -r ./optional-resources/requirements.txt`
## Usage
To use this program, run `python main.py`
## Executable
Use the python PyInstaller module to create an executable. Check the [documentation ](https://pyinstaller.readthedocs.io/en/stable/) for more details on how to use PyInstaller.
To create an executable of Sticky Notes, you will first need to edit the function call on line 94 to `createNewInstanceExe()` instead of `createNewInstance()`. Once you have done that and after you have installed PyInstaller, run `python -m PyInstaller --noconsole --onefile --icon=./optional-resources/stickyNotes.ico ./main.py`
## License
This projects is licensed under the GNU General Public License v3.0. Click [here](LICENSE) to view the license text.
## Screenshot
![Screenshot](https://user-images.githubusercontent.com/69877833/132151892-7ae65392-890d-4f95-a064-70577c21607a.PNG)<br>
Screenshot of Sticky Notes (while running)


