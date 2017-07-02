# Uses python3

import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    
    # print(dataset)
    
    digits = []
    ops = []
            
    for c in dataset:
        if c == '+' or c == '-' or c == '*':
            ops.append(c)
        else:
            digits.append(int(c))
    
    n = len(digits)
    
    max_res = [[0] * n for i in  range(n)]
    min_res = [[0] * n for i in  range(n)]
    
    for i in range(n):
        max_res[i][i] = digits[i]
        min_res[i][i] = digits[i]
        
    
    def min_and_max(i, j):
        min_val = sys.maxsize
        max_val = -sys.maxsize
        
        for k in range(i, j):
            a = evalt(max_res[i][k], max_res[k+1][j], ops[k])
            b = evalt(max_res[i][k], min_res[k+1][j], ops[k])
            c = evalt(min_res[i][k], min_res[k+1][j], ops[k])
            d = evalt(min_res[i][k], max_res[k+1][j], ops[k])
            
            min_val = min(min_val, a, b, c, d)
            max_val = max(max_val, a, b, c, d)
        
        return min_val, max_val
    
        
    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            min_res[i][j], max_res[i][j] = min_and_max(i, j)

    # print('min:')
    # for r in min_res:
    #     print(r)
    #     
    # print('max:')
    # for r in max_res:
    #     print(r)
            
    return max_res[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
