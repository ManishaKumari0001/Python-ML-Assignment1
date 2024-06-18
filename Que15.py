import csv

# CSV file path
file_path = 'que15.csv'

# Read data from the CSV file and print it to the console
with open("que15.csv", mode='r', newline='') as file:
    reader = csv.reader(file)
    print("Contents of the CSV file:")
    for row in reader:
        print(', '.join(row))


