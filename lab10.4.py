"""
4.	Write a program that asks the user to input his name 
and print its initials. Assuming that the user always types 
first name, middle name and last name and does not include 
any unnecessary spaces. For example, if the user enters 
Nina Marie Peterson the program should display N. M. P.
"""
user_name = input("Please enter your full name: ")
names = user_name.split()
initials_list = ""
for name in names:
    name_letters = list(name)
    initials_list += name_letters[0]
    initials_list += ". " #I added a space behind the period because that's what you did in your example output :)
print(initials_list)