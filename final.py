"""Read in the input file and determine the average pain (note: this will be a floating point number) 
for males in the post-operative suction group, males in the control group, females in the post-operative suction group, 
and females in the control group. Your program should include main and a function declared outside main to calculate the average. 
Your program should read in the input file. Parse the file. Calculate the appropriate averages and write the results to an output file (4 lines).  
Note the output file should designate what each of the averages is associated with.

The variables are:

id:  a patient identifier

trt:  1 is post-operative suction, 2 is control

sex: 1 is male, 2 is female

age: in years

pain: 0-4 scale where 0 is no pain, and 4 is the most severe

time: 1 is the first, 6 is the last measurement on each person"""

def main():
    male_po_pain = 0
    male_control_pain = 0
    female_po_pain = 0
    female_control_pain = 0
    male_po_count = 0
    male_control_count = 0
    female_po_count = 0
    female_control_count = 0
    input = open("final_shoulder.csv", "r")
    input.readline()
    for line in input:
        patient_info = line.split(',')
        id = patient_info[0]
        trt = patient_info[1]
        sex = patient_info[2]
        age = patient_info[3]
        pain = float(patient_info[4])
        time = patient_info[5]
        if sex == "1":
            if trt == "1":
                male_po_pain += pain
                male_po_count += 1
            else:
                male_control_pain += pain
                male_control_count += 1
        else:
            if trt == "1":
                female_po_pain += pain
                female_po_count += 1
            else:
                female_control_pain += pain
                female_control_count += 1
    input.close()
    output = open("final_output.txt", "w")
    output.write("The average pain for males in the post-operative suction group is:     " + str(average(male_po_pain, male_po_count)) + "\n")
    output.write("The average pain for males in the control group is:     " + str(average(male_control_pain, male_control_count)) + "\n")
    output.write("The average pain for females in the post-operative suction group is:     " + str(average(female_po_pain, female_po_count)) + "\n")
    output.write("The average pain for females in the control group is:     " + str(average(female_control_pain, female_control_count)) + "\n")
    output.close()

def average(pain_total, count):
    group_average = pain_total / count
    return round(group_average, 3)

main()