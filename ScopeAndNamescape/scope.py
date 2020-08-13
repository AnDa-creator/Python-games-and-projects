import time
def fact(n):
    """calculate n! iteratively"""
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
        return result

def rec_fact(n):
    """USING RECURSION"""
    if n> 1:
        return (n * rec_fact(n-1))
    else:
        return 1

def fib(n):
    """F(n) = F(n-1) + F(n-2)"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
def fibonacci(n):
    if n==0:
        result = 0
    elif n==1:
        result = 1
    else :
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


time_init = time.time()
for i in range(36):
    print(i, fibonacci(i))
time_init2 = time.time()
print("time taken for iterative approach ", time_init2-time_init)
for i in range(36):
    print(i, fib(i))
time_init3 = time.time()
print("time taken for recursive approach ", time_init3-time_init2)