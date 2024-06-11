def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option (1/2/3/4/5): ")

        if choice in {'1', '2', '3', '4'}:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")

            if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
                print("Invalid input. Please enter valid numbers.")
                continue

            num1 = float(num1)
            num2 = float(num2)

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result is: {result}")

        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
