number = int(input("Enter the number: "))
store = number
store1 = number
i = 0
j = 0
binary_num = 0
octal_num = 0
rem1 = number % 2
rem2 = number % 8
binary_num = binary_num + rem1 * (10**i)
octal_num = octal_num + rem2 * (10**j)
i += 1
j +=1
while (number // 2) != 0:
    number = number // 2
    rem = number % 2
    binary_num = binary_num + rem * (10**i)
    i += 1
while (store // 8) != 0:
    store = store // 8
    rem = store % 8
    octal_num = octal_num + rem * (10**j)
    j += 1
print("Decimal number:{} Binary form:{} "
      "Octal form:{}".format(store1, binary_num, octal_num))





