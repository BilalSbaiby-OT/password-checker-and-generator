import random
import sys
import os
import time 

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')





def password_generator(lenght,symbols,numbers,uppercase):
    charpool = "abcdefghijklmnopqrstuvwxyz"
    if symbols == "yes":
        charpool += "!@#$%^&*()_+"
    if numbers == "yes":
        charpool += "0123456789"
    if uppercase == "yes":
        charpool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    password = ""
    while len(password) < lenght:
        password += random.choice(charpool)
    print(password)
        

def password_checker(password):
    if len(password) >= 12 and password and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()_+" for c in password):
        print("password is  strong")
    elif len(password) <= 12 and password and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()_+" for c in password):
        print("password is  moderate")
    elif len(password) <= 10 and password  and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()_+" for c in password):
        print("password is  average")
    elif len(password)>= 8 and password and any(c.isupper() for c in password) and any(c.isdigit() for c in password) :
        print("password is  little bit weak")
    else:
        print("password is weak")




try:
    while True:
        print("[1] Generate a new password")
        print("[2] Check password strength")
        print("[3] Exit")

        option = int(input(">>"))
        if option == 1:
            length = int(input("Password length: "))
            include_uppercase = input("Include uppercase? yes/Enter: ")
            include_numbers = input("Include numbers? yes/Enter: ")
            include_symbols = input("Include symbols? yes/Enter: ")

            password_generator(length,include_uppercase,include_numbers,include_symbols)
            time.sleep(3)
            clear_terminal()

        elif option == 2:
            user_pass = input("Enter your password: ")
            password_checker(user_pass)
            time.sleep(3)
            clear_terminal()
        elif option == 3:
            sys.exit()




except ValueError:
    print("Invalid input. Please enter a number.")