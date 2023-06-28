#PROGRAM LIKE A SIMPLE CALCULATOR
#THAT DISPLAY THE REMAINDER

def divide (x, y):
    return x / y

print("My Simple Calculator! ")

op = input("OPeration: ")
if op == '1':
    num1 = float(input("Enter the 1st number! "))          
    num2 = float(input("Enter the 2nd number! "))
    print("The Remainder of the Numbers", (num1 / num2))

else:
    print('Invalid Syntax')
