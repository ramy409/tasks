
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
command = input("Enter command (add, sub, mult, div) or 'stop' to exit: ").strip().lower()#الاولي بتعمل انا تلغي المسافات و التانيه بتخلي الرحف كابتل 
if command == 'stop':
    print("Exiting the program. Goodbye!")
    exit()
elif command in ('add', 'sub', 'mult', 'div'):
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if command == 'add':
            print("Result:", add(num1, num2))
        elif command == 'sub':
            print("Result:", sub(num1, num2))
        elif command == 'mult':
            print("Result:", mult(num1, num2))
        elif command == 'div':
            print("Result:", div(num1, num2))
    except ValueError:
            print("Error: Please enter valid numbers.")
else:
    print("Invalid command. Please try again.")    