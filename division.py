def divide_numbers():
    try:
    # Write a program that asks the user to input two numbers and performs division on them. 
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

        print(f"The result is: {result}.")

    except ZeroDivisionError:
        print("Error: Cannot devide by 0")
    except ValueError:
        print("Please enter numeric values.")


divide_numbers()