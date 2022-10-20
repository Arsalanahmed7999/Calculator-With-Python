# Calculator with python 

# Additon

def add(a, b):
    return a+b

#Subtract
def subtract(a, b):
    return a-b

# Multiplication
def mul(a, b):
    return a*b

#Division
def division(a, b):
    return a/b


print('Choose Option 1 for additon')
print('Choose Option 2 for subtraction')
print('Choose Option 3 for multiplication')
print('Choose Option 4 for division')

while True:
    choice = (input('Enter options (1, 2, 3, 4) : \n'))
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print("You have chosen Addition")
        elif choice == '2':
            print("You have chosen Subtraction")
        elif choice == '3':
            print("You have chosen Multiplication")
        elif choice == '4':
            print("You have chosen Division")

        num1 = float(input('Enter first number: \n'))
        num2 = float(input('Enter second number: \n'))

        # if choice
        if choice == '1':
            print(f' {num1} + {num2} = {add(num1, num2)}')
        elif choice =='2':
            print(f' {num1} + {num2} = {subtract(num1, num2)}')
        elif choice == '3':
            print(f"{num1} * {num2} = {mul(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")

        next_calc = input('You want to continue calculating? (yes/no) \n')
        if next_calc == 'no':
            break
    else:
        print('Invalid Value')

