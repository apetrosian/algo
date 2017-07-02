#Uses python3
import sys
import math

def calc_len(p1, p2):
    return math.sqrt(((p1[0] - p2[0])**2) + ((p1[1] - p2[1])**2))
    
def closest_strip(points, d):
    
    n = len(points)
    
    points = sorted(points, key=lambda x: x[1])
    
    for i in range(n-1):
        if (points[i+1][1] - points[i][1]) < d:
            d = min(d, calc_len(points[i], points[i+1]))
    
    return d

def closest_pair(points):
        
    n = len(points)
    
    # print(points)
    
    if n == 1:
        return sys.maxsize
        
    if n == 2:
        return calc_len(points[0], points[1])
        
    m = n // 2
    
    p1 = closest_pair(points[m:])
    p2 = closest_pair(points[:m])
        
    # print(points)
    # print(p1, p2)
    
    d =  min(p1, p2)
    
    strip = []
    
    for i in range(n):
        if abs(points[i][0] - points[m][0]) < d:
            strip.append(points[i])
            
    return min(d, closest_strip(strip, d))

def minimum_distance(x, y):
        
    result = closest_pair(sorted(zip(x, y)))

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
