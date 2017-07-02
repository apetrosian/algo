# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def fibonacci_partial_sum(a, b):

        # pisano period for mod 10
        PISANO_PERIOD = 60

        a = a % PISANO_PERIOD
        b = b % PISANO_PERIOD

        result = 0

        previous = 0
        current  = 1

        for x in range(1, b+1):
            if x >= a:
                result += current
            previous, current = current, previous + current

        return result % 10

a, b = map(int, input().split())
print(fibonacci_partial_sum(a, b))
