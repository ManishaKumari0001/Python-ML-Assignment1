# calculate the sum of numbers in a list
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

input_numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string of numbers into a list of integers
numbers_list = list(map(float, input_numbers.split()))

# Calculate the sum of numbers in the list
sum_of_numbers = calculate_sum(numbers_list)

print(f"The sum of the numbers {numbers_list} is: {sum_of_numbers}")
