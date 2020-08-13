import sys

def division(first_num, second_num):
    return first_num/second_num


while True:
    initial = str(input("Something?? "))
    if initial.upper() == "Q":
        break
    first_num = input("Enter 1st number: ")
    second_num = input("ENter 2nd number: ")

    try:
        print("The division of {} by {} is {}".format(first_num, second_num,
                                                      division(int(first_num),int(second_num))))
    except (ArithmeticError, TypeError, ValueError):
        print("Something is wrong with your input ")
    else:
        print("Division performed successfully")
    finally:
        print("It is always executed")

    print("You can try again or quit")
