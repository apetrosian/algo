#Uses python3
import sys
import math

def extract_min(h):
    item = min(h)
    h.remove(item)
    return item[1]

def find(h, v):
    for i in range(len(h)):
        if h[i][1] == v:
            return True
    return False

def change_prio(h, v, p):
    for i in range(len(h)):
        if h[i][1] == v:
            h[i] = (p, v)

def build_graph(x, y, n):
    edges = [[] for i in range(n)]
    dist = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                edges[i].append(j)
                dist[i].append(calc_len(x[i], y[i], x[j], y[j]))
    return edges, dist

def calc_len(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

def minimum_distance(x, y):
    n = len(x)

    if n == 0:
        return 0

    edge, dist = build_graph(x, y, n)

    cost = [sys.maxsize] * n
    parent = [None] * n

    cost[0] = 0

    H = [(cost[i], i) for i in range(n)]

    while len(H):
        u = extract_min(H)

        for v in range(len(edge[u])):
            if find(H, edge[u][v]) and cost[edge[u][v]] > dist[u][v]:
                cost[edge[u][v]] = dist[u][v]
                change_prio(H, edge[u][v], cost[edge[u][v]])

    return sum(cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
