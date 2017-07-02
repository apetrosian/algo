# Uses python3
def edit_distance(s, t):

    # print(s, t)
        
    if s == t:
        return 0
    
    n = len(s)
    m = len(t)

    dist = [[0] * (n+1) for i in  range(m+1)]
    
    for i in range(n+1):
        dist[0][i] = i
        
    for i in range(m+1):
        dist[i][0] = i
        
        
    for j in range(1, n+1):
        for i in range(1, m+1):
            insertion = dist[i][j-1] + 1
            deletion = dist[i-1][j] + 1
            mismatch = dist[i-1][j-1] + 1
            match = dist[i-1][j-1]
            
            if s[j-1] == t[i-1]:
                dist[i][j] = min(insertion, deletion, match)
            else:
                dist[i][j] = min(insertion, deletion, mismatch)
            
    # for r in dist:
    #     print(r)
                
    return dist[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
