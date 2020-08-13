# list_1 = []
# list_2 = list()
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))

# if list_1 == list_2:
#    print("The lists are equal")

# print(list("The lists are equal"))
# this costructor(line 9) takes each character and forms a list

# even = [2, 4, 6, 8]
#
# another_even = even
# another_even = list(even) list constructor
# print(another_even == even)
# print(another_even is even)
# another_even.sort(reverse=True)  look out
# print(even)
# odd = [1, 3, 5, 7, 9]
# numbers = [even, odd]

# for number_set in numbers:
#    print(number_set)
#
#    for value in number_set:
#        print(value)
menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

#print(menu)

for meal in menu:
    if "spam" not in meal:
        for ingreds in meal :
            print(ingreds)
