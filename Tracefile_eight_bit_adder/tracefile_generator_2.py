f=open("TRACEFILE.txt","w")


for x in range(16):
 primes = {2,3,5,7,11,13}
 if x not in primes :

        f.write("{:04b} {} 1\n".format(x,0))
 else:
        f.write("{:04b} {} 1\n".format(x,1))

f.close()