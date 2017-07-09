# python3
import sys

def InverseBWT(bwt):
    
    result = ""
    
    n = len(bwt)
    
    sorted_idx = sorted(range(n), key=lambda x: bwt[x])
        
    r = 0
    
    for i in range(n):
        
        c = bwt[sorted_idx[r]]
        r = sorted_idx[r]
        result += c

    return result[1:] + result[0]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))