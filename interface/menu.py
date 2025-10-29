# interface/menu.py

import tkinter as tk
from tkinter import messagebox
from core import validation, database, hashing

class LoginApp:
    def __init__(self, root):
        #Initialize the main application window
        self.root = root
        self.root.title("Login System")
        self.root.geometry("300x200")
        self.root.resizable(False,False)

        #Ensure database is created or exists
        database.createDB() 

        #start in login mode by defualt
        self.isLoginMode = True 

        #Create widgets - labels, entries, buttons
        #Title Label
        self.label = tk.Label(root, text="Login", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        #Frame for labels and entries
        self.frame = tk.Frame(root)
        self.frame.pack(pady=5)

        #Username label and entry
        tk.Label(self.frame, text="Username:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.usernameEntry = tk.Entry(self.frame, width=20)
        self.usernameEntry.grid(row=0,column=1,padx=5,pady=5)

        #Password label and entry
        tk.Label(self.frame, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.passwordEntry = tk.Entry(self.frame, show="*", width=20)
        self.passwordEntry.grid(row=1, column=1, padx=5, pady=5)

        #Login/signup button
        self.actionButton = tk.Button(root, text="Login", command=self.login)
        self.actionButton.pack(pady=5)

        #toggle mode button
        self.toggleButton = tk.Button(root, text="Create an account", command=self.toggleMode)
        self.toggleButton.pack(pady=5)

    #Login function
    def login(self):
        #Gets user input from entries
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        if database.usernameExists(username) and hashing.hashCheck(password, username):
            messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    #Signup function
    def signup(self):
        #Gets user input from entries
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        #Validate Username
        userMsg = validation.usernameValid(username)
        if userMsg: 
            messagebox.showerror("Invalid Username:", userMsg)
            return

        #Validate Password
        passMsg = validation.passwordValid(password)
        if passMsg:
            messagebox.showerror("Invalid Password:", passMsg)
            return
        
        #Create new account
        hashWord = hashing.hashFunc(password)
        if database.addUser(username, hashWord):
            messagebox.showinfo("Success", "Account created successfully for {}.".format(username))
        else:
            messagebox.showerror("Error", "Failed to create account. Please try again.")



    #Toggle between login and signup modes
    def toggleMode(self):
        self.isLoginMode = not self.isLoginMode #toggles the mode

        if self.isLoginMode: #if in signup mode, switch to login mode
            self.label.config(text="Login")
            self.actionButton.config(text="Login", command=self.login)
            self.toggleButton.config(text="Create an account")
        else: #if in login mode, switch to signup mode
            self.label.config(text="Sign Up")
            self.actionButton.config(text="Sign Up", command=self.signup)
            self.toggleButton.config(text="Already have an acocunt?")

def launchApp():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()