# calculate age based on birth year
def calculate_age(birth_year):
    current_year = 2024  # Update this with the current year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)

print(f"You are {age} years old.")
