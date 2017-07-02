# Uses python3
def lcm(a, b):
    return (a*b) // gcd(a,b)

def gcd(a, b):
    if b > 0:
        return gcd(b, a % b)
    else:
        return a


a, b = map(int, input().split())
print(lcm(a, b))
