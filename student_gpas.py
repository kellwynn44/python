#Number of Old honor points = (Old Total Course Credits) * (Old Cumulative GPA)
#Number of New honor points = (CC1 *CS1) + (CC2 *CS2) + (CC3 *CS3) + (CC4 *CS4)
#Total Number of New Course Credits = CC1 + CC2 + CC3 + CC4
    #CC1= Course Credits for Course #1,
    #CS1= Course Grade Score for Course #1

new_file = open("Spring2021-LCSC-Student_GPAs.txt", "w")
new_file.write("Student ID    Cumulative GPA     Total Course Credits   Semester GPA   Semester Credits\n")
new_file.write("==========    ==============     ====================   ============   ================\n")
read_file = open("LCSC-Student_Grades.dat", "r")
read_file.readline()
for line in read_file:
    separated = line.split()   
    student_id = separated[0]
    cumulative_gpa = separated[1] 
    old_total_credits = separated[2] 
    CC1 = separated[3] 
    CS1 = separated[4] 
    CC2 = separated[5] 
    CS2 = separated[6] 
    CC3 = separated[7] 
    CS3 = separated[8] 
    CC4 = separated[9]   
    CS4 = separated[10] 
    new_honor_points = (int(CC1) * float(CS1)) + (int(CC2) *float(CS2)) + (int(CC3) * float(CS3)) + (int(CC4) * float(CS4))   
    old_honor_points = int(old_total_credits) * float(cumulative_gpa)
    new_semester_credits = int(CC1) + int(CC2) + int(CC3) + int(CC4)   #total credits here             
    new_total_credits = int(old_total_credits) + new_semester_credits
    new_semester_gpa = round((new_honor_points / new_semester_credits),2)
    honor_points = old_honor_points + new_honor_points
    new_cumulative_gpa = round((honor_points / new_total_credits),2)   
    new_file.write(student_id)
    new_file.write("           ")
    new_file.write(str(new_cumulative_gpa))
    new_file.write("                  ")
    new_file.write(str(new_total_credits))
    new_file.write("               ")  
    new_file.write(str(new_semester_gpa))
    new_file.write("               ") 
    new_file.write(str(new_semester_credits))
    new_file.write("\n")
new_file.close()
read_file.close()