"""
3.	Write a Python program that accepts a string from user. 
Your program should create a new string by shifting one position 
to left.
"""
user_string = input("Please enter a word or phrase: ")
string_letters = list(user_string)
string_letters.append(" ")
string_letters.append(string_letters[0])
string_letters.pop(0)
length = len(string_letters)
for i in range(length):
    print(string_letters[i], end="")