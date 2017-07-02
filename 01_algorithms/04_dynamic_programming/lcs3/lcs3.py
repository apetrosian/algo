#Uses python3

import sys

def lcs3(a, b, c):
    
    n = len(a) + 1
    m = len(b) + 1
    o = len(c) + 1
    
    matrix = [[[0 for k in range(o)] for j in range(m)] for i in range(n)]
        
    for i in range(n):
        for j in range(m):
            for k in  range(o):
                if i == 0 or j == 0 or k == 0:
                    pass
                elif a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                    matrix[i][j][k] = matrix[i-1][j-1][k-1] + 1;
                else:
                    t = max(matrix[i-1][j][k], matrix[i][j-1][k])
                    matrix[i][j][k] = max(t, matrix[i][j][k-1])

    # for row in matrix:
    #     print(row)
    
    return matrix[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
