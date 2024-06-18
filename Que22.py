# find the minimum and maximum values in a list
def find_min_max(numbers):
    if not numbers:
        return None, None  
    
    min_val = numbers[0]
    max_val = numbers[0]
    
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return min_val, max_val

input_numbers = input("Enter a list of numbers separated by spaces: ")

# Convert the input string of numbers into a list of floats
numbers_list = list(map(float, input_numbers.split()))

# Find the minimum and maximum values in the list
min_value, max_value = find_min_max(numbers_list)

print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
