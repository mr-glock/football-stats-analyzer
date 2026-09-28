def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/ b

num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
print("1. Add")
print("2. Subtract")
print("3. multiply")
print("4. Divide")
choice = int(input("Choose an operation (1-4):"))

if choice == 1:
    print(f"{num1} + {num2} = {add(num1,num2)}")
elif choice == 2:
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == 3:
    print(f" {num1} * {num2} = {multiply(num1, num2)}")
elif choice == 4:
    try:
        print(f"{num1}/{num2} = {divide(num1, num2)}")
    except:
        print("Cannot divide by zero")
    
else:
    print("invalid choice")


