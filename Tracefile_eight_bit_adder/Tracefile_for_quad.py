f=open("TRACEFILE.txt","w")


for x in range(16):
    num = ("{:04b}".format(x))
    print(num[1])
    if num[0] == "1" and num[2] == "1":
        f.write("{:04b} {:02b} 11\n".format(x,3))

    elif num[0] == "1" and num[2] == "0":
        f.write("{:04b} {:02b} 11\n".format(x,2))
    elif num[0] == "0" and num[2] == "1":
        f.write("{:04b} {:02b} 11\n".format(x,1))
    else :
        f.write("{:04b} {:02b} 11\n".format(x,0))


f.close()