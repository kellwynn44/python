"""
2.	Write a Python program that accepts a string from user. 
Your program should create a new string in reverse of first 
string and display it.
"""
user_string = input("Please enter a word: ")
string_letters = list(user_string)
string_letters.reverse()
length = len(string_letters)
new_string = ""
for i in range(length):
    new_string += string_letters[i]
print(new_string)