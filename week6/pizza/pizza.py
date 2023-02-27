import sys
import csv
from tabulate import tabulate

# Checks for one command line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# File name does not end in .py: sys.exit
if not (sys.argv[1].lower().endswith(".csv")):
    sys.exit("Not a CSV file")

# File does not exis: sys.exit
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

# Adding each row as a list in the csv
row_list = []

reader = csv.reader(file)
for row in reader:
    row_list.append(row)
file.close()

# Passing row_list as an argument to tabulate
print(tabulate(row_list, headers="firstrow", tablefmt="grid"))
