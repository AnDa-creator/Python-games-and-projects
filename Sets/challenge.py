# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.
text = input("enter the text here: ")
vowels = "AEIOUaeiou"
result = set()
for letter in text :
    if letter not in vowels :
        result.add(letter)
print(sorted(result))
print(type(result))
print(type(sorted(result)))