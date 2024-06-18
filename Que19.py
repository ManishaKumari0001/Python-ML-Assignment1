import string

# remove punctuation from a string
def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Use translate method to remove punctuation
    return input_string.translate(translator)

user_input = input("Enter a string with punctuation: ")

# Remove punctuation from the input string
cleaned_string = remove_punctuation(user_input)

print("String after removing punctuation:")
print(cleaned_string)
