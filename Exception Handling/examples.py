def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(4**82)
try:
    print(factorial(998))
except RecursionError:
    print("This program can't calculate factorials that large")
except ZeroDivisionError:
    print("Division by zero not possible")

print("Program terminating")
