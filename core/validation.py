#core/validation.py

from core import database

#validates username based on the following criteria:
#1. not empty
#2. between 3 or 24 character long
#3. only conatins letters and numbers
#4. does not already exist in the database
def usernameValid(username):
    if not username:
        print("\nError: Username cannot be empty.")
        return False
    elif len(username) < 3 or len(username) > 24:
        print("\nError: Username must be between 3 and 24 characters.")
        return False
    elif not username.isalnum():
        print("\nError: Username can only contain letters and numbers.")
        return False
    elif database.usernameExists(username) == True:
        print("\nError: Username already exists.")
        return False
    else:
        return True

#validates password based on the following criteria:
#1. not empty
#2. at least 6 characters long
#3. contains at least one uppercase letter, one lowercase letter, one number, and one special character
def passwordValid(password):
    if not password:
        print("\nError: Password cannot be empty.")
        return False
    elif len(password) < 6 or len(password) > 30:
        print("\nError: Password must be between 6 and 30 characters.")
        return False
    elif not any(char.isupper() for char in password): 
        print("\nError: Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
        return False
    elif not any(char.islower() for char in password): 
        print("\nError: Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
        return False
    elif not any(char.isdigit() for char in password): 
        print("\nError: Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
        return False
    elif not any(char in '!@#$%^&*()-_=+[]|;:,.<>?/' for char in password): 
        print("\nError: Password must contain at least one uppercase and lowercase letter,\none number, and one special character.")
        return False
    else:
        return True
