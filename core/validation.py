#core/validation.py

from core import database

#validates username based on the following criteria:
#1. not empty
#2. between 3 or 24 character long
#3. only conatins letters and numbers
#4. does not already exist in the database
def usernameValid(username):
    msg = ""
    if not username:
        msg = ("Username cannot be empty.")
    elif len(username) < 3 or len(username) > 24:
        msg = ("Username must be between 3 and 24 characters.")
    elif not username.isalnum():
        msg = ("Username can only contain letters and numbers.")
    elif database.usernameExists(username) == True:
        msg = ("Username already exists.")
    return msg

#validates password based on the following criteria:
#1. not empty
#2. at least 6 characters long
#3. contains at least one uppercase letter, one lowercase letter, one number, and one special character
def passwordValid(password):
    msg = ""
    if not password:
        msg = ("Password cannot be empty.")
    elif len(password) < 6 or len(password) > 30:
        msg = ("Password must be between 6 and 30 characters.")
    elif not any(char.isupper() for char in password): 
        msg = ("Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
    elif not any(char.islower() for char in password): 
        msg = ("Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
    elif not any(char.isdigit() for char in password): 
        msg = ("Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
    elif not any(char in '!@#$%^&*()-_=+[]|;:,.<>?/' for char in password): 
        msg = ("Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
    return msg
