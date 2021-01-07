"""

Check password - app that checks whether a string is a valid password
 The password rules are as follows:
 A passowrd must have at least eight characters
 A password must consist of only letters and digits
  A password must contain at least two digits
  Guidelines:
  Prompt the user to enter a password
  Display valid password if the rules are followed or invalid password otherwise

"""
import re

def main():
    while(True):
        p=input("Please type your password or press q button to exit...\n")
        if(p!="q"):
            if checkPass(p)==False:
                print("Your password must contain at least 1 alphabetic character , 1 number and minimum 8 characters.. ")
            else:
                print("Login Succesfully")
                break
        else:
            break

def checkPass(password):
    if len(password)<8:
        return False
    for i in range(len(password)):
        if not password[i].isdigit() and not password[i].isalpha():
            return False
    i=d=0
    for i in range(len(password)):
        if password[i].isdigit():
            d+=1
    if d<2:
        return False
    return True



main()
        
