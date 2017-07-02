#Uses python3

import sys

# from heapq import heappush, heappop

def extract_min(h):
    item = min(h)
    h.remove(item)
    return item[1]

def change_prio(h, v, p):
    # print('change_prio', h, v, p)
    for i in range(len(h)):
        if h[i][1] == v:
            h[i] = (p, v)

def distance(adj, cost, s, t):
    # print(adj, cost, s, t)

    n = len(adj)

    prev = [None] * n
    dist = [sys.maxsize] * n

    dist[s] = 0

    # build heap
    H = [(dist[i], i) for i in range(n)]

    # for i in range(n):
    #     heappush(H, (dist[i], i))

    while len(H):

        u = extract_min(H)

        print(u)

        for v in range(len(adj[u])):

            print(v, dist[adj[u][v]], dist[u], cost[u][v])

            if dist[adj[u][v]] > dist[u] + cost[u][v]:
                dist[adj[u][v]] = dist[u] + cost[u][v]
                prev[adj[u][v]] = u

                change_prio(H, adj[u][v], dist[adj[u][v]])

        # print(H)
        # print(prev)
        # print(dist)

    if dist[t] != sys.maxsize:
        return dist[t]
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
