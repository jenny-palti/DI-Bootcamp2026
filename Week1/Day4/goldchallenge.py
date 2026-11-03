# Daily Challenge Gold: Solve the Matrix - Week 1, Day 4

MATRIX_STR = '''7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Step 1: Turn the string into a 2D list (a list of rows, each row a list of characters)
matrix = []
for line in MATRIX_STR.split("\n"):
    matrix.append(list(line))

# Step 2: Read the matrix column by column, top to bottom, left to right
num_columns = max(len(row) for row in matrix)
characters = []
for col in range(num_columns):
    for row in matrix:
        if col < len(row):              # some rows are shorter, so skip missing cells
            characters.append(row[col])

# Steps 3 + 4: Keep only letters; a group of symbols BETWEEN two letters becomes one space
decoded_message = ""
symbols_since_last_letter = False

for char in characters:
    if char.isalpha():
        if symbols_since_last_letter and decoded_message != "":
            decoded_message += " "
        decoded_message += char
        symbols_since_last_letter = False
    else:
        symbols_since_last_letter = True

# Step 5: Print the decoded message
print(decoded_message)
