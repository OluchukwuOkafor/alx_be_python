# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the square pattern using nested loops
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next row
    row += 1
