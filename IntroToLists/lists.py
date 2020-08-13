# ipAddress = input("Please enter an ip address")
# print(ipAddress.count("."))
parrot_list = ["non pinin" , 'no more', 'a stiff', 'bereft of life']

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

if numbers == numbers_in_order:
    print("equal")
else :
    print("not equal")
numbers.sort()
if numbers == numbers_in_order:
    print("equal")
else :
    print("not equal")

