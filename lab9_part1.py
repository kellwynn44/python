"""
A palindrome is a string that reads the same backward as forward. 
For example, the words dad, madam and radar are all palindromes. 
Write a programs that determines whether the string is a palindrome.
"""

user_word = input("Please enter a word to check if it's a palindrome: ")
user_word = list(user_word)
second_copy_to_reverse = list(user_word)
reversed_list = second_copy_to_reverse
reversed_list.reverse()
#used lines 13 and 14 to debug
#print(user_word)        
#print(reversed_list)

if user_word == reversed_list:
    print("This word is a palindrome!")
else:
    print("Sorry, this word is not a palindrome.")