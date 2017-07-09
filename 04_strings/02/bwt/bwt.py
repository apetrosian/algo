# python3
import sys

def BWT(text):
    
    n = len(text)
    
    M = []
    
    result = ""
    
    for i in range(n):
        M.append( text[n-i:] + text[0:n-i] )
    
    for s in sorted(M):
        result += s[-1]

    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))