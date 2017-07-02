#Uses python3

def is_greater(x, y):

    ab = str(x) + str(y)
    ba = str(y) + str(x)

    if ab >= ba:
        return True
    else:
        return False

def largest_number(a):
    #write your code here
    res = []

    a = sorted(a)

    while len(a) > 0:

        max_digit = -1

        for x in a:

            if max_digit < 0:
                max_digit = x
            elif is_greater(x, max_digit):
                max_digit = x

        res.append(a.pop(a.index(max_digit)))

    return ''.join(map(str, res))

n = input()
data = list(map(int, input().split()))
print(largest_number(data))
