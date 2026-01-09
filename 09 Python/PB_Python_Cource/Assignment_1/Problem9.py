#Q.Ask the user for : Principal (p), Rate (R), Time(T). Convert all to float and compute simple interest :

#Formula = SI = (P*R*T)/100

p = float(input("Enter the Principal Amount : "))
r = float(input("Enter Rate of Interest : "))
t = float(input("Enter the period of time in years: "))

print("SI = ", (p*r*t)/100)
# Enter the Principal Amount : 25000
# Enter Rate of Interest : 8
# Enter the period of time in years: 1
# SI =  2000.0

#print("SI = ", (p*r*t/12)/100) if the time period entered would bee in months
# Enter the Principal Amount : 25000
# Enter Rate of Interest : 8
# Enter the period of time in months: 6
# SI =  1000.0





