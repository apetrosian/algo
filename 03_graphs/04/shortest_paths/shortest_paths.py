#Uses python3

import sys
import queue

def belman_ford(H, s, t, n, cost, add):

    prev = [None] * n
    dist = [sys.maxsize] * n

    dist[s] = 0

    q = [s]

    for i in range(n + add):

        if len(q):
            u = q.pop()
        else:
            break

        for v in range(len(H[u])):

            q.insert(0, H[u][v])

            if dist[H[u][v]] > dist[u] + cost[u][v]:

                dist[H[u][v]] = dist[u] + cost[u][v]
                prev[H[u][v]] = u

    return dist[t]


def shortet_paths(adj, cost, s, distance, shortest):

    n = len(adj)

    for i in range(n):
        distance[i] = belman_ford(adj, s, i, n, cost, -1)

    for i in range(n):
        shortest[i] = distance[i] - belman_ford(adj, s, i, n, cost, n+i)

    print(distance)
    print(shortest)


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
    s = data[0]
    s -= 1
    distance = [sys.maxsize] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, shortest)
    for x in range(n):
        if distance[x] == sys.maxsize:
            print('*')
        elif shortest[x] > 0:
            print('-')
        else:
            print(distance[x])
