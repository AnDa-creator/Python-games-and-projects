
def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)

def build_tuple(*args):
    return args

if __name__ == '__main__':
    message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
    print(type(message_tuple))
    print(message_tuple)

