# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    
    pairs = []
    
    for start in starts:
        pairs.append((start, 'l'))
        
    
    for end in ends:
        pairs.append((end, 'r'))
        
    
    for i in range(len(points)):
        pairs.append((points[i], 'p', i))
    
    p = 0
        
    for pair in sorted(pairs):
        if pair[1] == 'l':
            p += 1
        elif pair[1] == 'r':
            p -= 1
        else:
            cnt[pair[2]] = p
        
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
