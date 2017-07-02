# Uses python3
import sys

def get_majority_element(a, n):

    a = sorted(a)

    count = 0
    el = -1

    majority = n / 2


    for i in range(n):


        if el != a[i]:
            if count > majority: return count

            el = a[i]
            count = 0

        count += 1

    if count >majority:
        return count
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # assert n == len(a), 'Wrong input!'
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
