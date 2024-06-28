# Define the add function
def add(x, y):
    return x + y

# Define the subtract function
def subtract(x, y):
    return x - y

# Define the multiply function
def multiply(x, y):
    return x * y

# Define the divide function
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Display the menu to the user
def print_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# Main function to run the calculator
def calculator():
    while True:
        print_menu()
        
        # Take input from the user
        choice = input("Enter choice(1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()
