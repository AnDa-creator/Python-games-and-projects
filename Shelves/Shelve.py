import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making soda"
fruit['lemon'] = "a sour, yellow sour fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"
# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["line"] = "great with tequila"
#
# for snack in fruit:
#     print(snack +": " + fruit[snack])
# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#     description = fruit.get(shelf_key, "We don't have a "+ shelf_key)
#     print(description)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
#
# fruit.close()

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()
