import tkinter as tk
import pickle


class LoginManager:

    

    def __init__(self):
        

        # Creates a window
        login_info_window = tk.Tk()

        # Stores the directory of the pickle file that will hold our login data
        self.LOGIN_DATA_FILE = "login_data.pkl"
        
        self.tumblr_username = tk.StringVar()
        self.tumblr_password = tk.StringVar()

        # Unused as of now
        self.bsky_username = tk.StringVar()
        self.bsky_password = tk.StringVar()
        self.reddit_username = tk.StringVar()
        self.reddit_password = tk.StringVar()


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
        tk.Entry(login_info_window, textvariable = self.tumblr_username).pack()

        # Tumblr Password
        tk.Label(login_info_window, text="Password").pack()
        tk.Entry(login_info_window, textvariable = self.tumblr_password).pack()

        # Save button
        tk.Button(login_info_window, text="Save", command=self.serializeData).pack()

        # Loops the window
        login_info_window.mainloop()





    # Saves a dict of passwords and usernames
    def serializeData(self):

        # Organizes all of the login data into a dict
        login_data = {
            "tumblr_username": self.tumblr_username.get(),
            "tumblr_password": self.tumblr_password.get()
        }
        pickle.dump(login_data, open(self.LOGIN_DATA_FILE, mode='wb'))
        print("Data Saved")
    
    # Reads the data from the save file as a dict
    def deserializeData(self):
        return pickle.load(open(self.LOGIN_DATA_FILE, 'rb'))
        
