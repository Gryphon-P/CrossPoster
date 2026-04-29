import tkinter as tk
from PIL import Image, ImageTk
import pickle
import FileGUI
import Tumblr
import subprocess

# Creates a root for tk
tk_root = tk.Tk()

# Makes the window title
tk_root.title("OpenCrossposter")

# Sets the window's minsize
tk_root.minsize(400, 300)

# Makes main text at top
tk.Label(tk_root, text="OPEN CROSSPOSTER").pack()
tk.Label(tk_root, text="* * *").pack()

# Makes the button to edit the login info
def editLoginInfo():
    subprocess.run(["python", "LoginManager.py"]) # SO janky but it works
tk.Button(tk_root, text="Edit Login Info", command=editLoginInfo).pack()

# Makes the button to make a post
tk.Button(tk_root, text="Make Post", command=FileGUI.getFile).pack()

# Loops the window
tk_root.mainloop()
