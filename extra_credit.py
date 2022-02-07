#add course 1, course 3, and course 4 credits to each student's previous credit total

new_file = open("Spring2021-LCSC-Student_Credits.txt", "w")
new_file.write("Student ID    Earned Credits\n")
new_file.write("==========    ==============\n")
read_file = open("LCSC-Student_Grades.dat", "r")
read_file.readline()
for line in read_file:
    separated = line.split()   
    student_id = separated[0]
    old_total_credits = separated[2] 
    CC1 = separated[3] 
    CC3 = separated[7] 
    CC4 = separated[9]   
    new_semester_credits = int(CC1) + int(CC3) + int(CC4)               
    new_total_credits = int(old_total_credits) + new_semester_credits   #debug note: the student on line 20 of the .dat file
    new_file.write(student_id)                                          #is found on line 21 of the new .txt file
    new_file.write("           ")
    new_file.write(str(new_total_credits))
    new_file.write("\n")
new_file.close()
read_file.close()