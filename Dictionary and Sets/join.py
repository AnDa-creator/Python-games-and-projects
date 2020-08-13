locations = {0: "you are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building , a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
dic1 = {"Q": 0}
dic2 = {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}
dic3 = {"N": 5, "Q": 0}
dic4 = {'W': 1, "Q": 0}
dic5 = {"N": 1, "W": 2, "Q": 0}
dic6 = {"W": 2, "S": 1, "Q": 0}
exits = {0: dic1,
         1: dic2,
         2: dic3,
         3: dic4,
         4: dic5,
         5: dic6
         }
vocabulary = { "QUIT": "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST": "E",
               "WEST": "W"}
print(locations[0].split())
print(locations[3].split(","))

# loc = 1
# while True:
#     availableExits = ""
#     for direction in exits[loc].keys():
#         availableExits += direction + ", "
#     print((locations[loc]))
#     if loc == 0:
#         break
#     direction = input("Available exits are "+ availableExits).upper()
#
#     print()
#     if len(direction) > 1:
#         for word in vocabulary:
#             if word in vocabulary:
#                 direction = vocabulary[word]
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")



