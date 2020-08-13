import random


def creator(len, dict, pass_list):
        password = ""

        for num in range(1,len + 1):
            password += dict[random.randint(0,60)]
        if password in pass_list:
            pass
        return password


if __name__ == '__main__':
    dict = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    pass_list = []
    with open("Passwords.txt", 'w') as pass_file:
        for i in range(1,10**10):
            pass_new = creator(8, dict, pass_list)
            pass_list += pass_new
            print(pass_new, end='\n', file=pass_file)
            print(i, " ",pass_new, end='\n')






