# convert a string into a list of its characters
def string_to_char_list(string):
    return list(string)

input_string = input("Enter a string: ")
char_list = string_to_char_list(input_string)
 
print("The list of characters is:", char_list)
