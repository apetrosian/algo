# Uses python3

def get_change(m):
    #write your code here

    coins = 0

    while m >= 10:
        m -= 10
        coins += 1

    while m >= 5:
        m -= 5
        coins += 1

    return coins + m

m = int(input())
print(get_change(m))
