#Uses python3

def largest_number(n):
    #write your code here
    res = []

    k = n
    l = 1

    while k > 2*l:
        res.append(l)
        k -= l
        l += 1

    res.append(k)

    return res

if __name__ == '__main__':
    n = int(input())
    res = largest_number(n)
    print(len(res))
    print(' '.join(map(str,res)))
