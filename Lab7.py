#Print the avg cumulative GPA of students >= 50 credits
cumulative_gpa_for_high_credit_students = 0
count = 0
new_file = open("lab7_output.txt", "w")
new_file.write("Average Cumulative GPA for all students that have completed 50 or more credits:     ")
read_file = open("LCSC-Student_Grades.dat", "r")
read_file.readline()
for line in read_file:
    separated = line.split()   
    cumulative_gpa = separated[1]           #cumulative gpa for student
    total_credits = separated[2]        #total credits for student
    if int(total_credits) >= 50:
        cumulative_gpa_for_high_credit_students += float(cumulative_gpa)
        count += 1  
avg_cumulative_gpa = round(cumulative_gpa_for_high_credit_students / count, 2)
new_file.write(str(avg_cumulative_gpa))
new_file.write("\n\nTotal number of students with 50 or more credits:  ")
new_file.write(str(count))
new_file.close()
read_file.close()