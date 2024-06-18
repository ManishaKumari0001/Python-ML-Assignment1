# convert a string to title case
def title_case(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Initialize an empty list to store words in title case
    title_case_words = []
    
    # Capitalize the first letter of each word and append to the list
    for word in words:
        title_case_words.append(word.capitalize())
    
    # Join the title case words into a single string
    title_case_string = ' '.join(title_case_words)
    
    return title_case_string

user_input = input("Enter a string to convert to title case: ")

# Convert the string to title case
title_case_output = title_case(user_input)

print("Title case conversion:")
print(title_case_output)
