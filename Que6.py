# file name
file_name = "manisha.txt"

# Read the content of the file and print it to the console
try:
    with open(file_name, "r") as file:
        content = file.read()
        print("Content of the file:")
        print(content)
except FileNotFoundError:
    print(f"The file {file_name} does not exist.")
