# copy contents from one file to another
def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as src:
            contents = src.read()
        
        # Open the destination file in write mode
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        
        print(f"Contents of '{source_file}' have been copied to '{destination_file}' successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

copy_file(source_file, destination_file)
