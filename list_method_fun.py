"""Using your favorite LCSC-Student_grades.dat file read in the total course credits column 
and insert each of those credits into a list. Using the sum and length methods 
(note: len for length) compute the average of the total course credits list.  
Print the average to an output file. Also find the max and min of the total 
course credits list and write those to the file."""

credits_list = []
total = 0

output_file = open("output2.txt", "w")
read_file = open("LCSC-Student_Grades.dat", "r")
#read_file = open("testing.txt", "r") -- I used this to "debug" to ensure my code performed correctly
read_file.readline()
for line in read_file:
    data = line.split()
    total += int(int(data[2]))
    credits_list.append(int(data[2]))
total_credits = sum(credits_list)
num_in_list = len(credits_list)
avg = round(total_credits / num_in_list, 2) #I didn't see that you wanted the average in a specific format, 
max_of_list = max(credits_list)             #but there were so many digits that I decided to round the answer
min_of_list = min(credits_list)             #I hope this was okay to do
output_file.write("Average of the total course credits:  ")
output_file.write(str(avg))
output_file.write("\nMaximum of the total course credits:  ")
output_file.write(str(max_of_list))
output_file.write("\nMinimum of the total course credits:  ")
output_file.write(str(min_of_list))
output_file.close()
read_file.close()