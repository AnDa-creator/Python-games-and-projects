name = input("Please enter your name: ")
age = int(input("What is your age, {}? ".format(name) ))
if 18<= age <31:
    print("Welcome to the Holiday")
else:
    print("Sorry you aren't eligible")