#Q.Write a python program using function to convert Celsius to Fahrenheit.

def cel_to_fah(c):
    print(f"{c} Celcius in Fahrenheit is {(c * 1.8) + 32}")

c = float(input("Enter Celsius : "))
cel_to_fah(c)
