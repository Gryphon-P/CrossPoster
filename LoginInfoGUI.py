import tkinter as tk
import pickle


# Stores the directory of the pickle file that will hold our login data
LOGIN_DATA_FILE = "user_data.pkl"


def loginInfoGUI():

    # Creates a window
    login_info_window = tk.Tk()


    # Makes the window title
    login_info_window.title("Login Info Form")

    # Sets the window's minsize
    login_info_window.minsize(400, 300)

    # Makes main text at top
    tk.Label(login_info_window, text="LOGIN INFO").pack()
    tk.Label(login_info_window, text="* * *").pack()


    # Creates a input section for Tumblr
    tk.Label(login_info_window, text="").pack()
    tk.Label(login_info_window, text="TUMBLR").pack()

    # Tumblr Password
    tk.Label(login_info_window, text="Username").pack()
    tumblr_username = tk.StringVar()
    tk.Entry(login_info_window, textvariable = tumblr_username).pack()

    # Tumblr Password
    tk.Label(login_info_window, text="Password").pack()
    tumblr_password = tk.StringVar()
    tk.Entry(login_info_window, textvariable = tumblr_password).pack()

    # Save button
    tk.Button(login_info_window, text="Save").pack()

    # Loops the window
    login_info_window.mainloop()




# # Saves a dict of passwords and usernames
# def saveDict(savedata):
#     pickle.dump(savedata, open(file=LOGIN_DATA_FILE, mode='wb'))
#     print("Data Saved")




loginInfoGUI()