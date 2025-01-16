# Read and print rows of a CSV file
import csv
file_path = input("Enter the CSV file path: ")
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)