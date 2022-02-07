"""
3.	Write a program in python that accepts a string to setup a password. 
    Your entered password must meet the following requirements:
•	The password must be at least eight characters long.
•	It must contain at least one uppercase letter.
•	It must contain at least one lowercase letter.
•	It must contain at least one numeric digit.
"""

contains_number = False
contains_uppercase = False
contains_lowercase = False

user_password = input("""Please type a password that\'s at least 8 characters long,
                        has at least one uppercase letter, 
                        has at least one lowercase letter, 
                        and has at least one numeric digit:  """)

length = len(user_password)
user_password_array = list(user_password)

for i in range(length):
    user_password_array[i]
    if user_password_array[i].isnumeric():
        contains_number = True
    elif user_password_array[i].isupper() and user_password_array[i].isalpha:
        contains_uppercase = True
    elif user_password_array[i].islower() and user_password_array[i].isalpha:
        contains_lowercase = True

if contains_number and contains_uppercase and contains_lowercase and length >= 8:
    print("Valid Password")
else:
    print("Inv")
        