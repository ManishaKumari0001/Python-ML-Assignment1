def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))

# Check for non-negative input
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and display the factorial
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
