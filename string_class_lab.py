lower_count = 0
upper_count = 0
my_string = "Roses are Red, Violets are Blue"
for char in my_string:
    if char.islower():
        lower_count += 1  
    elif char.isupper():
        upper_count += 1
print("There are {} lowercase characters.".format(lower_count))
print("There are {} uppercase characters.".format(upper_count))


my_string = "The brown dog jumps over the lazy fox"
reversed_string = ""
index = len(my_string) - 1
while index >= 0:
  reversed_string += my_string[index]
  index -= 1
print(reversed_string)


original_string = "THE BROWN DOG JUMPS over the lazy fox"
modified_string = ""
for char in original_string:
  if char.islower():
    modified_string += char.upper()
  else:
    modified_string += char.lower()
print("The original string is: {}".format(original_string))
print("The modified string is: {}".format(modified_string))


my_string = "The Brown Dog Jumps Over The Lazy Fox"
vowels = "aeiou"
count = 0
for char in my_string:
  if char.lower() in vowels:
    count += 1
if count == 1:
    print("There is 1 vowel in the string")
else:
    print("There are {} vowels in the string".format(count))




##########################################################
# coding challenge
##########################################################
my_string = "" #example entered Hello
vowels = "aeiou"
modified_string = ""
for char in my_string:
  if char.lower() in vowels:
    modified_string += "*"
  else:
    modified_string += char
print(modified_string)  #example output was H*ll*

my_string = "Hobbes"
vowels = "aeiou"
#solution using replace method
for vowel in vowels:
    my_string = my_string.replace(vowel, "*")
print(my_string)