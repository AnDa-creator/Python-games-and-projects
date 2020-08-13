print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("please enter number to be squared "))

squares = []
squares = {number**2 for number in numbers}

print(squares)