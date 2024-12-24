def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if '.' in num1:
    num1 = float(num1)
else:
    num1 = int(num1)

if '.' in num2:
    num2 = float(num2)
else:
    num2 = int(num2)

if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    result = "Invalid input"

if isinstance(result, float) and result.is_integer():
    result = int(result)

print(f"Result: {result}")