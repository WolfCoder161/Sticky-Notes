import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import POPUP_BUTTONS_YES_NO
import subprocess

sg.theme("darkblue2")

layout=[
    [sg.Multiline("", key="note",autoscroll=True,tooltip="StickyNotes writing pad", focus=True, size=(50,20), disabled=False, text_color="black", background_color="#fffdcc", font=("Lucida Console", 12))],
    [sg.Button("Save", button_color="#4ec315"),sg.Button("Open"),sg.Button("New Note"), sg.Button("Close", button_color="#d30e16")]
    
]

window = sg.Window("StickyNotes",layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True, return_keyboard_events=True, element_justification="c", background_color="#ead42b", button_color="#da9c00", resizable=True, icon="./optional-resources/stickyNotes.ico").finalize()

def closeWin():
    content = values["note"]
    if docSaved == False:
        if len(content) > 1:
            userConsent = sg.popup_yes_no("Do you want to save your work?", keep_on_top=True, background_color="#f9923a", button_color="#da9c00", text_color="black", non_blocking=False)
            if userConsent == "Yes":
                saveWork = saveDoc()
            else:
                secondCheck = sg.popup_yes_no("Are you sure you don't want to save your work?", keep_on_top=True, background_color="#f9923a", button_color="#da9c00", text_color="black", non_blocking=False)
                if secondCheck == "No":
                    saveDoc()

def openDoc():
    pWindow = sg.Window("Sticky Notes",no_titlebar=True,layout=[[sg.Input(key='_FILEBROWSE_', enable_events=True, visible=False), sg.FileBrowse("Browse File", file_types=[("text files", "*.txt")], target="_FILEBROWSE_", enable_events=True), sg.Button("Open")],[sg.Button("Cancel")]], keep_on_top=True, element_justification="c",  background_color="#f9923a", button_color="#da9c00", return_keyboard_events=False)
    while True:
        pEvent, pValues = pWindow.read()
        if pEvent== "Open":
            filePath = pValues["_FILEBROWSE_"]
            if len(filePath)  >= 1:
                break
        if pEvent == "Cancel":
            filePath = "Null"
            break
    pWindow.close()
    if filePath != "Null":
        with open(filePath, "r") as file:
            fileC = file.read()
            window["note"].Update(fileC)
            file.close()
        docSaved = True
        docPath = filePath
    elif filePath == "Null":
        return "Null"

def saveDoc():
    if docSaved == True:
        with open(docPath, "w") as fileW:
            fileW.write(values["note"])
            fileW.close()
        sg.popup_quick_message("File saved\n" + docPath, keep_on_top=True, background_color="#56ef6a", text_color="black")
    else:
        filePath = ""
        lWindow = sg.Window("", layout=[[sg.Input(key='_SAVELOC_', enable_events=True, visible=False), sg.FileSaveAs("Save Location", default_extension=".txt", target="_SAVELOC_"), sg.Button("Save")],[sg.Button("Cancel")]], keep_on_top=True, background_color="#f9923a", button_color="#da9c00", no_titlebar=True, element_justification="c")
        while True:
            lEvent, lValues = lWindow.Read()
            if lEvent == "Cancel":
                break
            if lEvent == "Save":
                filePath = lValues["_SAVELOC_"]
                if len(filePath) >= 1:
                    with open(filePath, "w") as fileW:
                        fileW.write(values["note"])
                        fileW.close()
                    sg.popup_quick_message("File saved\n" + filePath, keep_on_top=True, background_color="#56ef6a", text_color="black")
                    break
        lWindow.close()

def createNewInstance():
    cFilePath = __file__
    subprocess.Popen(["Python", cFilePath])

def createNewInstanceExe():
    import sys
    cFilePath = sys.argv[0]
    subprocess.Popen([cFilePath])

docSaved = False
docPath = ""

while True:
    event, values = window.read()
    if event == "Close":
        closeWin()
        break
    if event == "Open":
        openDoc()
    if event == "Save":
        saveDoc()        
    if event == "New Note":
        createNewInstance()
window.close()