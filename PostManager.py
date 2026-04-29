import tkinter as tk
from PIL import Image, ImageTk
import FileGUI
from tkinter.scrolledtext import ScrolledText




# Creates a window
post_manager_window = tk.Tk()

 # Makes the window title
post_manager_window.title("Post Manager")

# Sets the window's minsize
post_manager_window.minsize(400, 300)

# Makes main text at top
tk.Label(post_manager_window, text="POST MANAGER").pack()
tk.Label(post_manager_window, text="* * *").pack()
tk.Label(post_manager_window, text="").pack()


# Manages images in a post
image_dirs = []
tk.Button(post_manager_window, text="Add Image", command=FileGUI.getFile).pack()

# Manages the main text
tk.Label(post_manager_window, text="").pack()
tk.Label(post_manager_window, text="MAIN TEXT").pack()
main_text = tk.StringVar()
ScrolledText(post_manager_window, wrap=tk.WORD, height=10).pack()

# Manages the tags
tk.Label(post_manager_window, text="").pack()
tk.Label(post_manager_window, text="TAGS").pack()
tags = tk.StringVar()
ScrolledText(post_manager_window, wrap=tk.WORD, height=1).pack()


# Holds what platforms we want to post to
post_tumblr = tk.BooleanVar()
post_bsky = tk.BooleanVar()
post_reddit = tk.BooleanVar()
tk.Label(post_manager_window, text="").pack()
tk.Label(post_manager_window, text="").pack()
tk.Checkbutton(post_manager_window, text="Post on Tumblr", variable=post_tumblr).pack()
tk.Checkbutton(post_manager_window, text="Post on Bsky", variable=post_bsky).pack()
tk.Checkbutton(post_manager_window, text="Post on Reddit", variable=post_reddit).pack()

# Post button
tk.Label(post_manager_window, text="").pack()
tk.Label(post_manager_window, text="").pack()
tk.Button(post_manager_window, text="POST").pack()

# Keeps the window running
post_manager_window.mainloop()
