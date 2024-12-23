def simple_calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == "5":
            print("Exiting Calculator")
            break

        if choice in ["1","2","3","4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == "2":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == "3":
                print(f"Result: {num1} x {num2} = {num1 * num2}")
            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid choice. Please pick a number between 1 and 5")

if __name__ == "__main__":
        simple_calculator()

