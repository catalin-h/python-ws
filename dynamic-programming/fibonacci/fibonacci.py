import sys

def fibonacci(n):
    previous = 1
    current = 1

    for _ in range(n - 2):
        next = previous + current
        current, previous = next, current

    return current

n=10
if len(sys.argv) == 2:
    n = int(sys.argv[1])

print(f'The {n}-th fibonacci number: ', fibonacci(n))
