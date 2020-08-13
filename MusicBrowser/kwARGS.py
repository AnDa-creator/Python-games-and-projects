def print_backwards(*args, end=' ', **kwargs):
    for word in args[::-1]:
        print(word[::-1], file=backwards,end=' ', **kwargs)
    print()


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')

