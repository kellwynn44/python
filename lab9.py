my_string = "SHIFT" 
my_letters = list(my_string)
letter_count = len(my_letters) #could also use: letter_count = len(my_string)
                                                #But I'm trying to keep track of what my program is doing :)
for i in range(len(my_letters) + 1): 
    print("")    
    if i >= 1:       
        for j in range(i, len(my_letters)):      
            print(my_letters[j], end="") 
        for k in range(i):
            print(my_letters[k], end="")        
    else:
        for i in range(len(my_letters)):
            print(my_letters[i], end="")

    
#extra code that accepts any string a user enters until the user gets tired of entering words
#because I figured why not :D
print("\n\n")

my_string = input("Please enter a word OR type exit to leave this program: ")      
while my_string != "exit":
    my_string = my_string.upper()  #ensures that string contains all uppercases so output is formatted as shown in the example
    my_letters = list(my_string)
    letter_count = len(my_letters)
    for i in range(len(my_letters) + 1): 
        print("")    
        if i >= 1:       
            for j in range(i, len(my_letters)):      
                print(my_letters[j], end="") 
            for k in range(i):
                print(my_letters[k], end="")        
        else:
            for i in range(len(my_letters)):
                print(my_letters[i], end="")    
    print("")
    my_string = input("Please enter another word OR type exit to leave this program: ")