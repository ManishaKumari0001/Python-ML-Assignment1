# check if a substring is present in a string
def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

# main string
main_string = input("Enter the main string: ")

# substring to search for
substring = input("Enter the substring to check: ")

# Check if the substring is present in the main string
if check_substring(main_string, substring):
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is NOT present in the main string.")
