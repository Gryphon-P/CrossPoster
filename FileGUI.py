from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Uses a gui to get a file directory
def getFile() -> str:

    # Hides the full GUI, only showing what we need
    Tk().withdraw()

    # Gets the filename from the GUI
    filename = askopenfilename()

    return filename