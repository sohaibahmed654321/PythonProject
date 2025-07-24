import random
import string
import sys
from random import choice

import pyperclip

my_password= []
print("----- Ramdom Password Generator -----")
pswd_length = int(input("Enter Password length : "))

if pswd_length < 8 or pswd_length > 20:
    print("Password Minium Length is 8 and Maximum Length is 20")
    sys.exit()

else:
    Password_list = string.ascii_letters + string.digits + string.punctuation
    for a in range(pswd_length):
        my_password.append(random.choice(Password_list))

    string_pswd = "".join(my_password)
    print(f"Generated Password : {string_pswd}")

    choice = input(f"Do You Want To Copy {string_pswd} ?")
    if choice.lower() == "yes":
        pyperclip.copy(string_pswd)
        print("Password Has Been Copied")
