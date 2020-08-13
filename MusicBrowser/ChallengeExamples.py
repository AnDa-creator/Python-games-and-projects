def avg_len(*args):
    count = 0
    wrd_count = 0
    for arg in args:
        for word in arg:
            count += 1
            list1=list(str(word))
            wrd_count += len(list1)
    try:
        return (wrd_count/count)
    except ZeroDivisionError:
        return "please provide some words"



if __name__ == '__main__':
    print(avg_len(("hello", "planet", "earth", "take", "me", "to", "your", "leader")))