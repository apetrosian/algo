# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def calc_pisano_period(m):
    a, b = 0, 1
    c = a + b

    for p in range(6 * m):
        c = (a + b) % m
        a, b = b, c

        if a == 0 and b == 1:
            return p+1

def get_fibonacci_huge(n, m):

    pisano_period = calc_pisano_period(m)

    result = calc_fib(n % pisano_period)

    return result % m

n, m = map(int, input().split())
print(get_fibonacci_huge(n, m))
