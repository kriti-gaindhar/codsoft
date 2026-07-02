import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot calculate modulus by zero.")
    return x % y

def exponent(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def calculator():
    print("--- Robust Python Calculator ---")
    print("Operations: +, -, *, /, %, ^ (exponent), sqrt")
    print("Type 'exit' to quit the program.")

    while True:
        print("\n------------------------------")
        operation = input("Enter operation: ").strip().lower()

        if operation == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        try:
            if operation == 'sqrt':
                val = float(input("Enter number: "))
                result = square_root(val)
                print(f"Result: {result}")
            
            elif operation in ['+', '-', '*', '/', '%', '^']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == '+':
                    result = add(num1, num2)
                elif operation == '-':
                    result = subtract(num1, num2)
                elif operation == '*':
                    result = multiply(num1, num2)
                elif operation == '/':
                    result = divide(num1, num2)
                elif operation == '%':
                    result = modulus(num1, num2)
                elif operation == '^':
                    result = exponent(num1, num2)
                
                print(f"Result: {result}")
            
            else:
                print("Error: Invalid operation selected.")

        except ValueError as ve:
            print(f"Input Error: {ve}")
        except ZeroDivisionError:
            print("Math Error: Division or Modulus by zero is not allowed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()