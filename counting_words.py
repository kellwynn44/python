"""
Ask the user for the name of a file. 
Read in the file and count the number of words 
(in a separate function called from main). 
Write the number of words to a file called output.txt
"""

def main():
    file_name = input("What file would you like to open?")
    counter(file_name)

def counter(file_name):
    word_count = 0
    infile = open(file_name, "r")
    for line in infile:
        words = line.split()
        word_count += len(words)
    infile.close()
    outfile = open("counting_words_output.txt", "w")
    outfile.write(str(word_count))
    outfile.close()

main()