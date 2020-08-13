import timeit
text = "what have the romans ever done for us"

capitals = """[char.upper() for char in text]"""
print(capitals)

# use map
map_capitals = """list(map(str.upper, text))"""
print(map_capitals)

words = """[word.upper() for word in text.split(' ')]"""
print(words)

#use map
map_words = """list(map(str.upper, text.split(" ")))"""
print(map_words)

result_1 = timeit.timeit(capitals, globals=globals(), number=10000)
result_2 = timeit.timeit(map_capitals, globals=globals(), number=10000)
result_3 = timeit.timeit(words, globals=globals(), number=10000)
result_4 = timeit.timeit(map_words, globals=globals(), number=10000)
print("time taken using char and comp is {}".format(result_1))
print("time taken using char and map is {}".format(result_2))
print("time taken using word and comp is {}".format(result_3))
print("time taken using word and map is {}".format(result_4))