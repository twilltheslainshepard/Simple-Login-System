# interface/menu.py

from core import validation
from core import database
from core import hashing

#Prompts user to choose between login, signup, or exit
def displayMenu():
    print("Welcome")
    print("Choose between the following options\n")
    print("[1] Login")
    print("[2] Create Account")
    print("[3] Exit\n")
    while True:
        rawInput = input("Enter Choice: ")
        
        try:
            userInput = int(rawInput)
        except ValueError:
            print("Error, enter a number.")
            continue 

        if(userInput in [1,2,3]):
            return userInput 
        else:
            print("Error, wrong value, try again...")

#Checks if input for username is valid, if not prompts user to re-enter username
def usernameInput():
    while True:
        username = input("Create Username: ")
        if validation.usernameValid(username):
            return username
        else:
            continue #loop again    

#Checks if ipnut for password is valid, if not prompts user to re-enter username
def passwordInput():
    while True:
        password = input("Create Password: ")
        if validation.passwordValid(password):
            return password
        else:
            continue # loop again

#Prompts user to enter username and password to create an account
def signupMenu():
    database.createDB() #Check for / create database
    print("\nSignup Menu")
    print("Please enter the following details to create an account.\n")
    username = usernameInput()
    password = passwordInput()
    hashword = hashing.hashFunc(password)
    database.addUser(username, hashword)

#Promts user to enter username and password to login
def loginMenu():
    print("\nLogin Menu")
    print("Please enter your login details.\n")

    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if database.usernameExists(username) and hashing.hashCheck(password, username):
            print(f"Login Successful! Welcome back, {username}!")
            return
        else:
            print("Error: Invalid username or password, try again...\n")
            continue #loop again
    