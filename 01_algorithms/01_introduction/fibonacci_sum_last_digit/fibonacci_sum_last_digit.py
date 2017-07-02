# Uses python3

def fibonacci_sum(n):

    if (n <= 1):
        return n

    # pisano period for mod 10
    PISANO_PERIOD = 60

    result = 0

    previous = 0
    current  = 1

    n = n % PISANO_PERIOD

    for x in range(1, n+1):
        result += current
        previous, current = current, previous + current

    return result % 10

n = int(input())
print(fibonacci_sum(n))
