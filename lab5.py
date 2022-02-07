x = 0.25 #AA
y = 0.5  #AB
z = 0.25 #BB
p = 1/2 * (y/(y+z)) #.333
g = 1

print("Generation      AA      AB     BB")
print("==========     ====    ====    ====")
#print the starting values of x, y, and z as generation 1
print("        " + str(g) + "      " + str(x) + "    " + str(y) + "    " + str(z))
#increment g by 1 so the loop starts at the second generation
g += 1
while z <= 0.99: 
    x = p**2
    y = 2 * p * (1 - p)
    z = (1 - p)**2
    p = 1/2 * (y/(y+z)) #the value of p needs to change each time through the loop
    print("        " + str(g) + "      " + str(round(x,3)) + "    " + str(round(y,3)) + "    " + str(round(z,3)))
    g += 1