# count the occurrences of a specific element in a list
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

input_list = input("Enter a list of elements separated by spaces: ")

# Convert the input string of elements into a list
elements_list = input_list.split()

# specific element to count
element_to_count = input("Enter the element to count: ")

# Count the occurrences of the specific element in the list
occurrences = count_occurrences(elements_list, element_to_count)

print(f"The element '{element_to_count}' occurs {occurrences} times in the list.")
