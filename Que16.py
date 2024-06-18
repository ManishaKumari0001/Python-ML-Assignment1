# count frequency of each character in a string
def count_characters(input_string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Count frequency of each character
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency

user_input = input("Enter a string: ")

# Count the frequency of each character in the input string
frequency_dict = count_characters(user_input)

print("Character frequencies:")
for char, freq in frequency_dict.items():
    print(f"'{char}' : {freq}")
