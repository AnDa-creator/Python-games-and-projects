def prime_nums():
    current = 2
    count = 0
    while True:
        yield current
        while True:
            current += 1
            for val in range(1, current):
                print(val)
                if current % val == 0:
                    count += 1
            if count == 1:
                break


def odd_nums():
    current = 1
    while True:
        yield current
        current += 2

def pi_series():
    odds = odd_nums()
    approximation = 0
    while True:
        approximation += (4/ next(odds))
        yield approximation
        approximation -= (4/ next(odds))
        yield approximation

approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))