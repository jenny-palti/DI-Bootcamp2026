# 1. Ask for User Input:
# The string must be exactly 10 characters long.
# 2. Check the Length of the String:
# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:
# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:
# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.

string = input("Tell me a word: ")
string = 'banana'
if len(string) < 10:
    print("String not long enough.")
elif len(string) > 10:
    print("String too long.")
else:
    print("Perfect string")

for i in range(1, len(string) + 1):
    print(string[:i]) 