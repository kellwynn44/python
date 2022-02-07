user_string = input()
letter = list(user_string)
new_string = [""]
length = len(letter)
for i in range(length):
    if letter[i] == "<" or letter[i] == ">" or letter[i] == "\\":
        new_string.append("\\") 
        new_string.append(letter[i])
    else:
        new_string.append(letter[i])
new_length = len(new_string)
for i in range(new_length):
    print(new_string[i], end="")