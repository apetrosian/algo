#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0

    for i in range(len(a)):

        max_a = max(a)
        max_b = max(b)

        res += max_a * max_b

        a.pop(a.index(max_a))
        b.pop(b.index(max_b))

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
