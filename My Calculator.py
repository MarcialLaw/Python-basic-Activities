print("My Calculator")
print("1 = add")
print("2 = subtraction")
print("3 = multiplication")
print("4= division")

op = input("Operation: ")
if op == '1':
    num1 = int(input('Enter a number!: '))
    num2 = int(input('Enter a number!: '))
    print("The sum of the Numbers", (num1 + num2)) 

elif op == '2':
    num1 = int(input('Enter a number!: '))
    num2 = int(input('Enter a number!: '))
    print("The product of the Numbers", (num1 - num2))

elif op == '3':
    num1 = int(input('Enter a number!: '))
    num2 = int(input('Enter a number!: '))
    print("The Qoutient of the Number", (num1 * num2))

elif op == '4':
    num1 = int(input('Enter a number!: '))
    num2 = int(input('Enter a number!: '))
    print("The Remainder of the Numbers", (num1 / num2))
    
    
else:
    print('invalid operator!')
