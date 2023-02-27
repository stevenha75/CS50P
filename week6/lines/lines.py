import sys

# Checks for one command line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# File name does not end in .py: sys.exit

if not (sys.argv[1].lower().endswith(".py")):
    sys.exit("Not a Python file")

# File does not exis: sys.exit
try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")

# Read & count non-empty/comment lines
line_counter = 0

lines = file.readlines()
for line in lines:
    if not line.lstrip().startswith("#"):
        if line.isspace() == False:
            line_counter += 1

# Print number of lines
print(line_counter)

