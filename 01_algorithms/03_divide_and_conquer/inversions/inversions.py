# Uses python3
import sys

def merge(left, right):
    
    res = []
    inversions = 0
    
    # print('merge:', left, right)
    
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            inversions += len(left)
            res.append(right.pop(0))
    
    if left:
        res = res + left
    
    if right:
        res = res + right
        
    # print('merge res:', res)
    return res, inversions
            

def merge_sort(arr, i):
    n = len(arr)
    
    # print(arr)

    if n == 1:
        return arr, i
        
    mid = n // 2
    
    left, i = merge_sort(arr[:mid], i)
    right, i = merge_sort(arr[mid:], i)
    
    res, inv = merge(left, right)
        
    i = i + inv
    
    return res, i
    

def get_number_of_inversions(arr):
        
    res, number_of_inversions = merge_sort(arr, 0)
    
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # print(merge_sort(a))
    print(get_number_of_inversions(a))
