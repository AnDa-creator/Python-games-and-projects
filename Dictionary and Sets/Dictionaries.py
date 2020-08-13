fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "round and crunchy"}
#print(fruit)
#print(fruit['lemon'])
#fruit["pear"]= "an odd shaped apple"
#print(fruit)
#del fruit["lemon"]
#print(fruit)
#fruit.clear()
print(fruit)
#while True:
#    dict_key = input("Please enter a fruit: ")
#    if dict_key == "quit":
#         break
#    description = fruit.get(dict_key, "We don't have a " + dict_key)
#    print(description)
    #if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    #else:
    #    print("We don't have a " + dict_key)
# for i in range(10):
#    for snack in fruit:
#        print(snack + " is "+ fruit[snack])
#    print('-'*40)

#ordered_key = sorted(list(fruit.keys()))
#for f in ordered_key:
#    print(f+" - "+ fruit[f] )
# print('-'*50)
# for f in fruit.keys():
#    print(f+" - " + fruit[f])
# for key in fruit:
#   print(fruit[key])
#print(fruit.keys[])

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit['tomato'] = 'not nice with ice-cream'
# print(fruit_keys)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    items, description =snack
    print(items + " is "+ description)
print(dict(f_tuple))





