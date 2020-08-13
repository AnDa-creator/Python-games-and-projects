import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
turn = 1
while guess != answer:
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher: ")
    else:
        print("Please guess lower: ")
    guess = int(input())
    turn += 1
if guess != 0:
    print("You have guessed correctly on turn no. {}".format(turn))
else:
    print("game over")
