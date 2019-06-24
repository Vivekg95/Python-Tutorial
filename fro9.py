
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
import sys

sys.setrecursionlimit(5000)

def factorial1(m):
    if m == 1:
        return 1
    else:
        return m * factorial(m-1)

print(factorial(30))
