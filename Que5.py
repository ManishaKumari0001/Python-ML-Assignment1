# string input
user_input = input("Enter a string: ")

# Specify the file name
file_name = "manisha.txt"

# Write the string to the file
with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to {file_name}.")
