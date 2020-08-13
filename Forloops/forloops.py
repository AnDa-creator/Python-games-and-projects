number = "9,223,214,227,225,207,236,230,210"
cleanednumber=''
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanednumber= cleanednumber+number[i]
newNumber= int(cleanednumber)
print("The number is {} ".format(newNumber))
for i in number :
    print(i,end='')
print()
for state in ["not pinin' ", "no more", "a stiff", "benefit of lift"]:
    print("This parrot is "+state +" ",end="\t")
    print("this parrot is {}".format(state))
for i in range(0,100,5):
    print("i is {}".format(i),end=", ")