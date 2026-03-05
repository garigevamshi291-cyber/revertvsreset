# Simple Python Program

def greet(name):
    print("Hello,", name)
    print("Welcome to Python programming!")

def add_numbers(a, b):
    return a + b

# Main program
name = input("Enter your name: ")
greet(name)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)
print("The sum is:", result)
