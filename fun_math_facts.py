#Print the following:
#0 X 0 = 0
#0 X 1 = 1
#....
#1 X 10 = 10
#...
#10 X 0 = 0
#10 X 1 = 10
#....
#10 X 10 = 100
for i in range(11):
    for j in range(11):
        print(str(i) + " X " + str(j) + " = " + str(i*j))