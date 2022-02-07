loan_amount = float(input("Enter Amount Borrowed: ")) #L
loan_duration = int(input("Enter Loan Duration in Months: ")) #Y
interest_rate = float(input("Enter Interest Rate: ")) #R
#interest_rate = float(input("Enter Interest Rate: ")) / 100 #R
#I commented out the above and used the version on line 3 because the input test value for the interest rate was already 0.03
#The instructions said "The interest rate should be converted from percentage to a fractional value"

#P = (L*(R*(1+R)**Y)) / ((1+R)**Y -1)
monthly_payment = (loan_amount * (interest_rate * (1 + interest_rate)**loan_duration)) / ((1 + interest_rate)**loan_duration - 1)
txt = "{:.2f}"
print(txt.format(monthly_payment))
print("")

print("Month   Principal     Interest     Principal     New Balance")
print("                      Payment      Payment                  ")
print("=====   =========     ========     =========     ===========")
print("    " + str(0) + "   " + txt.format(loan_amount) + "         " 
            + txt.format(0) + "         " + txt.format(0)
            + "       " + txt.format(loan_amount))
current_balance = loan_amount
for i in range(1,9):  #range should be (1,loan_duration+1) to view the "loan balance over the payment period"; however I tailored it so my output would look the requested output
    interest_payment = current_balance * interest_rate #I = current * R
    principal_payment = monthly_payment - interest_payment #C = P - I
    new_balance = current_balance - principal_payment #new = old - C   
    print("    " + str(i) + "   " + txt.format(current_balance) + "      " 
            + txt.format(interest_payment) + "      " + txt.format(principal_payment)
            + "       " + txt.format(new_balance))
    current_balance = new_balance #current = new