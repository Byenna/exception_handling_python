# exception_handling_python
Exercises to practice exception handling in Python

Here's a simple exercise to practice exception handling for beginners:
Write a program that asks the user to input two numbers and performs division on them. However, include exception handling to handle any potential errors that may occur during the division process. Specifically, handle the following exceptions:
1. ZeroDivisionError: If the user enters 0 as the second number, display an error message saying "Error: Cannot divide by 0.".
2. ValueError: If the user enters a non-numeric value as either the first or second number, display an error message saying "Error: Invalid input. Please enter numeric values."
Here's a sample solution in Python:

```
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

        print("The result is:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by 0.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

divide_numbers()

```

In this solution, we use the `try-except` block to handle potential exceptions that may arise during the division process. The `ZeroDivisionError` exception is handled when the user enters 0 as the second number, and the `ValueError` exception is handled when the user enters a non-numeric value. If no exception occurs, the division is performed successfully and the result is printed.
I hope this exercise helps you practice exception handling! Let me know if you have any further questions.