# Initialize an empty list to store lines of input
lines = []
print("Enter multiple lines of input. Press Enter without typing anything to finish:")

# Continue reading input until an empty line is entered
while True:
    line = input()
    if line == "":
        break  # Exit the loop if an empty line is entered
    lines.append(line)  # Add the line to the list of lines

print("\nThe entered lines are:")
for line in lines:
    print(line)
