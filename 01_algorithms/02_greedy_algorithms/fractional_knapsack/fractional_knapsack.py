# Uses python3
import sys


def get_value_per_unit(w, v):

    return v / w

def get_optimal_value(n, capacity, weights, values):
    value = 0
    # write your code here

    # value per unit
    p = []

    for i in range(n):
        p.append(values[i] / weights[i])

    while capacity > 0 and len(p) > 0:
        next_item_index = p.index(max(p))
        p.pop(next_item_index)

        if capacity >= weights[next_item_index]:

            value += values[next_item_index]
            capacity -= weights[next_item_index]

            values.pop(next_item_index)
            weights.pop(next_item_index)

        else:
            part = weights[next_item_index] / capacity
            value += values[next_item_index] / part
            capacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))
