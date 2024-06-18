# calculate the sum of digits of a number
def sum_of_digits(number):
    digits = str(number)
    digit_sum = 0
    for digit in digits:
        digit_sum += int(digit)
    return digit_sum

number = int(input("Enter a number: "))

result = sum_of_digits(number)
print(f"The sum of digits of the number {number} is: {result}")
