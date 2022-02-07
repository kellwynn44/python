HOURLY_WAGE = 15.00
WEEKS_PER_YEAR = 52
NORMAL_WORKWEEK_HOURS = 40


name = input("Please enter your name: ")
employee_type = input("Please enter S if you are a salary employee or H if you are an hourly employee: ")

if employee_type == 's' or employee_type == 'S':
    salary = input("Please enter your annual salary without a dollar sign or any commas: ")
    weekly_salary = float(salary) / WEEKS_PER_YEAR
    print(name + " is a salary worker who makes $" + str(round(weekly_salary, 2)) + " per week.")
elif employee_type == 'h' or employee_type == 'H':
    hours_worked = input("Please enter the number of hours you worked this week: ")
    hours_worked = int(hours_worked)
    if hours_worked <= NORMAL_WORKWEEK_HOURS:
        weekly_pay = hours_worked * HOURLY_WAGE
        print(name + " is an hourly wage worker who made $" + str(round(weekly_pay, 2)) + " this week.")
    else:
        weekly_pay = NORMAL_WORKWEEK_HOURS * HOURLY_WAGE + ((hours_worked - NORMAL_WORKWEEK_HOURS) * (HOURLY_WAGE * 1.5))
        print(name + " is an hourly wage worker who made $" + str(round(weekly_pay, 2)) + " this week.")

user_input = input("Enter Y if you want to enter another employee's information or N to quit: ")
while user_input != 'N' and user_input != 'n':
    #if user_input == 'Y' or user_input == 'y':
    #the above code would ensure the program only runs for a 'y' or 'Y' entry; however, you didn't ask for this so I took it out and fixed my indenting
    name = input("Please enter employee's name: ")
    employee_type = input("Please enter S if " + name + " is a salary employee or H if " + name + " is an hourly employee: ")
    if employee_type == 's' or employee_type == 'S':
        salary = input("Please enter " + name + "'s" + " annual salary without a dollar sign or any commas: ")
        weekly_salary = float(salary) / WEEKS_PER_YEAR
        print(name + " is a salary worker who makes $" + str(round(weekly_salary, 2)) + " per week.")
        user_input = input("Enter Y if you want to enter another employee's information or N to quit: ")
    elif employee_type == 'h' or employee_type == 'H':
        hours_worked = input("Please enter the number of hours " + name + " worked this week: ")
        hours_worked = int(hours_worked)
        if hours_worked <= NORMAL_WORKWEEK_HOURS:
            weekly_pay = hours_worked * HOURLY_WAGE
            print(name + " is an hourly wage worker who made $" + str(round(weekly_pay, 2)) + " this week.")
            user_input = input("Enter Y if you want to enter another employee's information or N to quit: ")
        else:
            weekly_pay = NORMAL_WORKWEEK_HOURS * HOURLY_WAGE + ((hours_worked - NORMAL_WORKWEEK_HOURS) * (HOURLY_WAGE * 1.5))
            print(name + " is an hourly wage worker who made $" + str(round(weekly_pay, 2)) + " this week.")
            user_input = input("Enter Y if you want to enter another employee's information or N to quit: ")
    #else:
        #break
            #these two lines were used to end the program correctly when the user entered anything besides N, n, Y, or y