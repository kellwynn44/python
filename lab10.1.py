"""
1.	Write a Python program that accepts a string from user. 
Your program should create and display a new string where the 
first and last characters have been exchanged.
"""
user_string = input("Please enter a word: ")
string_letters = list(user_string)
length = len(string_letters)
string_letters.append(string_letters[0])
string_letters.pop(0)
string_letters.insert(0, string_letters[length - 2]) #the string has increased by 1 BUT the length variable has NOT
string_letters.pop(length - 1) #so if original word's length was 3 -> pop(2) NOT pop(3) BUT string_letters now has indexes 0,1,2,3
for i in range(length):
    print(string_letters[i], end="")
