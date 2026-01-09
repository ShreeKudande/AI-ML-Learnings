#Q.Take a decimal number as input (like 45.78) and output it:
#integer part = 45
#Fractional Part = .78

dec_num = float(input("Enter the decimal number : "))

print("Integer part - ", int(dec_num))

fra_par = dec_num - int(dec_num)
print("Fractional part - ", round(fra_par, 10))

# Enter the decimal number : 45.78
# Integer part -  45
# Fractional part -  0.78


