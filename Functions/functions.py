def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep =' ', end='\n', file=None, flush=False):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return  " " * left_margin + text


# with open("Centred.txt", mode = 'w') as centred_file:
# call the function
with open("menu", "w") as menu:
    print(centre_text("spam and eggs"), file=menu)
    print(centre_text("spam,spam and eggs"), file=menu)
    print(centre_text("spam, spam, spam, and eggs"), file=menu)
    print(centre_text(12), file=menu)
    print(centre_text("first", "second", 3, 4, "spam"), file=menu)

# print('='+ str(12 * 3))
# print(sorted(["b", "d", "c", "a"]))

