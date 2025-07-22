import random as rd
import sys
import string

# city_names = ["karach","quetta","lahore","sukkur","multan","rawalpindi","islamabad","peshawar","swat","faislabad"]
#
# print(city_names)
# print(rd.sample(city_names, 3))
# rd.shuffle(city_names)
# print(city_names)
# print(rd.choice(city_names))

# print("********** Random Number Guessing Game ********\n")
# computer_num = rd.randint(1,20)
# Lives = 3
#
# while Lives > 0:
#     user_input = int(input("Enter Any Number Between 1 to 20 : "))
#
#     if user_input == computer_num:
#         print("Congratulations You've Guessed!!")
#         sys.exit()
#
#     else:
#         Lives -= 1
#
#         if user_input > computer_num:
#             print("* Hint : Think Lower Number")
#         elif user_input < computer_num:
#             print("* Hint : Think Higher Number")
#
#         if Lives == 0:
#             print("Lives End")
#         else:
#             print(f"{Lives} Remaining")

print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
print(string.whitespace)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)
