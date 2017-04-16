#Recursion


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

print("5!={}, 3!{}, 11!={}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))


def fibonacci(limit):
    numbers = []
    current = 0
    next_number = 1

    while current < limit:
        current, next_number = next_number, next_number + current
        numbers.append(current)

    return numbers

print('fibonacci')
for n in fibonacci(100):
    print(n, end=', ')


def fibonacci_co(limit):
    current = 0
    next_number = 1

    while current < limit:
        current, next_number = next_number, next_number + current
        yield current

print()
print('fibonacci_co')
for n in fibonacci_co(100):
    print(n, end=', ')