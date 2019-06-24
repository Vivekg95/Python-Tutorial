# Define a filename.
import os.path
filename = "C:\\Users\\Vivek Kumar\\Desktop\\python10\\from.py"
if not os.path.isfile(filename):
    print('File does not exist.')
else:

# Open the file as f.
# The function readlines() reads the file.
    with open(filename) as f:
        content = f.read().splitlines() #readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
    for line in content:
        print(line)