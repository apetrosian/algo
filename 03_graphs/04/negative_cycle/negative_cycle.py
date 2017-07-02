#Uses python3

import sys

def belman_ford(H, s, n, cost):

    prev = [None] * n
    dist = [sys.maxsize] * n

    dist[s] = 0

    q = [s]

    for i in range(n):

        if len(q):
            u = q.pop()
        else:
            break

        for v in range(len(H[u])):

            q.insert(0, H[u][v])

            if dist[H[u][v]] > dist[u] + cost[u][v]:
                dist[H[u][v]] = dist[u] + cost[u][v]
                prev[H[u][v]] = u

    return dist[s]


def negative_cycle(adj, cost):

    n = len(adj)

    for i in range(len(adj)):
        if belman_ford(adj, i, n, cost) < 0:
            return 1

    return 0


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
    print(negative_cycle(adj, cost))
