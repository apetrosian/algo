# Uses python3
def gcd(a, b):
    if b > 0:
        return gcd(b, a % b)
    else:
        return a

a, b = map(int, input().split())
print(gcd(a, b))
