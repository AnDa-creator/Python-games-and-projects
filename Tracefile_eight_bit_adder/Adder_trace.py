f = open('Adder_trace.txt', "w")

for x in range(256):


    for y in range(256):
        f.write("{:08b}{:08b} {:08b} 11111111\n".format(x, y, (x + y) % 256))

f.close()

