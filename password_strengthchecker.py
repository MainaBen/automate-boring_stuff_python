"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that
is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string
against multiple regex patterns to validate its strength.
from Chapter 7: Automae Broing Staff
"""
import re
def password_checker():
    password = input("Enter your password: ")
    while True:
        if len(password) < 8:
            print('Invalid Password. Password needs to be 8 characters or more')
            break
        #This logic uses positive look ahead to check for number and letters
        lowerReg = re.compile(r"(?=.*[a-z])")
        lg = lowerReg.search(password)
        if lg == None:
            print("Invalid Password. Password needs at least one lowercase letter")
            break
        
        upperReg = re.compile(r'(?=.*[A-Z])')
        res = upperReg.search(password)
        if res == None:
            print('Invalid Password. Password needs at least one upper case letter')
            break
        
        digitreg = re.compile(r'(?=.*\d)')
        drg = digitreg.search(password)
        if drg == None:
            print('Invalid password. Password needs to have at least one digit')
            break
        else:
            print('Valid Password. ')
            break
  

password_checker()

