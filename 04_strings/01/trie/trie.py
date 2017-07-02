#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):

    # for p in patterns:
    #     print(p)

    # init root node
    tree = dict()

    nodes = 1

    for p in patterns:

        current_node = 0

        for i in range(len(p)):

            if current_node not in tree:
                tree[current_node] = {}

            # print(tree)

            if p[i] in tree[current_node]:
                current_node = tree[current_node][p[i]]
            else:
                tree[current_node][p[i]] = nodes
                current_node = nodes
                nodes += 1


    # for node in tree:
    #     print(node, tree[node])

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
