import shelve

with shelve.open("loc_data", writeback=True) as loc_info:
    loc = 1
    while True:
        availableExits = ", ".join(loc_info["locations"][loc]["exits"].keys())

        print(loc_info["locations"][loc]["desc"])

        if loc == 0:
            break
        else:
            allExits = loc_info["locations"][loc]["exits"].copy()
            allExits.update(loc_info["locations"][loc]["namedExits"])

        direction = input("Available exits are " + availableExits).upper()
        print()

    # Parse the user input, using our vocabulary dictionary if necessary
        if len(direction) > 1:  # more than 1 letter, so check vocab
            words = direction.split()
            for word in words:
                if word in loc_info["vocabulary"]:   # does it contain a word we know?
                    direction = loc_info["vocabulary"][word]
                    break

        if direction in allExits:
            loc = allExits[direction]
        else:
            print("You cannot go in that direction")
