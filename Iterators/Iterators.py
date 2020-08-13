string = "1234567890"

# for char in string:
#    print(char)
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

#for char in string:
#    print(char)
#for char in iter(string):
#    print(char)
my_list = ["Hello, ", "I ", "used ", "to ", "think ",
           "that ", "I ",
           "am ", "the ", "dumbest ", "person ", "alive."]
my_iterator = iter(my_list)

for i in range(len(my_list)):
    print(next(my_iterator),end=' ')
