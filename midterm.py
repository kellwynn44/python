mlb_total = 0
al_total = 0
nl_total = 0

new_file = open("midterm_output.txt", "w")
new_file.write("2021 Postseason Batting Averages\n")
new_file.write("AL Batting Average   NL Batting Average    Overall Batting Average\n")
new_file.write("###                  ###                   ###\n")
read_file = open("midterm_input.txt", "r")
read_file.readline()
for line in read_file:
    separated = line.split()
    mlb_total = mlb_total + float(separated[len(separated) -1])#need to use len() to find the length of the array (to be able to point to the last index in the array) because some team names contain more spaces than others
    league = separated[len(separated) -2] 
    if league == "AL":
        al_total += float(separated[len(separated) -1]) 
    else:
        nl_total += float(separated[len(separated) -1]) 
read_file.close()
overall_avg = mlb_total / 10
nl_avg = nl_total / 5
al_avg = al_total / 5
new_file.write(str(round(al_avg, 3)))
new_file.write("                 ")
new_file.write(str(round(nl_avg, 3)))
new_file.write("                 ")
new_file.write(str(round(overall_avg, 3)))
new_file.close()