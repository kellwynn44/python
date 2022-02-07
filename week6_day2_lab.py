cs_gpa = 0
cs_count = 0
kin_gpa = 0
kin_count = 0
math_gpa = 0
math_count = 0
web_gpa = 0
web_count = 0
total_count = 0
i = 0

name = input("Please enter your name or type quit to exit the program: ")
while name != "quit":   
    major = input("Please enter your major: ")
    if major == "CS":
        gpa = float(input("Please enter your GPA: "))
        cs_gpa += gpa
        cs_count += 1
        total_count += 1
    elif major == "KIN":
        gpa = float(input("Please enter your GPA: "))
        kin_gpa += gpa
        kin_count += 1
        total_count += 1
    elif major == "MATH":
        gpa = float(input("Please enter your GPA: "))
        math_gpa += gpa
        math_count += 1
        total_count += 1
    else: 
        gpa = float(input("Please enter your GPA: "))
        web_gpa += gpa
        web_count += 1
        total_count += 1
    name = input("Please enter your name or type quit to exit the program: ")
print("Major   Avg.GPA \n_______________ \n_______________ ")
print("CS     " + str(cs_gpa / cs_count))
print("KIN    " + str(kin_gpa / kin_count))
print("MATH   " + str(math_gpa / math_count))
print("WEB    " + str(web_gpa / web_count))