# python3

from random import randint


def hash_func(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans

def precompute_hashes(text, len_p, prime, x):
    len_t = len(text)

    H = [0] * (len_t - len_p + 1)

    H[len_t - len_p] = hash_func(text[-len_p:], prime, x)

    y = 1

    for i in range(1, len_p + 1):
        y = (y * x) % prime

    for i in range(len_t - len_p - 1, -1, -1):
        #print(text, i, text[i], text[i + len_p])
        H[i] = ((x * H[i+1]) + ord(text[i]) - (y * ord(text[i + len_p]))) % prime

    return H


def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))


def are_equal(s1, s2):
    #print(s1, s2)
    if s1 == s2:
        return True
    else:
        return False

def get_occurrences(pattern, text):

    result = []

    prime = 1000007
    x = randint(1, prime - 1)

    H = precompute_hashes(text, len(pattern), prime, x)

    p_hash = hash_func(pattern, prime, x)

    for i in range(0, len(text) - len(pattern) + 1):
        #if p_hash == hash_func(text[i:i + len(pattern)]):
        if H[i] == p_hash:
            if are_equal(text[i:i + len(pattern)], pattern):
                result.append(i)

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
