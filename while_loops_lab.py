
"""The assignment was make a list of ten names. 
Make a list of 10 majors and then using a single 
while loop iterate through both lists and print them 
in the following format:
1. Student: Michelle Major: CS
2. Student: Bob Major: MATH"""
from os import name


output_file = open("outputFile.txt", "w")
names = ["Michelle", "Anna", "Leo", "Beth", "Paul", "Elizabeth", "Travis", "Mark", "Erin", "Glen"]
majors = ["CS", "ENGL", "MATH", "PN", "CHEM", "AC", "POLS", "BIOL", "ART", "ENGR"]
length_names = len(names)
length_majors = len(majors)
i = 0
student = "Student: "
major = "Major: "

while(i < length_names):
    num = i + 1
    print("% s. % s % s       % s % s" % (num, student, names[i], major, majors[i]))
    output_file.write(str(num))
    output_file.write(". Student: ")
    output_file.write(str(names[i]))
    output_file.write("        Major: ")
    output_file.write(str(majors[i]))
    output_file.write("\n")
    i += 1

"""Note to Nina: I didn't know if you meant print to the terminal 
or print to a text document, so I made my code do both :)
I also used abbreviations from the LCSC course catalog for the majors"""