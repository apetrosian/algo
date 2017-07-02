# python3
import sys

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

def prefix_matching(text, trie):
	# print(text)

	v = trie[0]

	for i in range(len(text)):
		if text[i] in v:
			# not leaf
			if v[text[i]] in trie:
				v = trie[v[text[i]]]
			else:
				return True
		else:
			return False

	return False

def solve (text, n, patterns):
	result = []

	trie = build_trie(patterns)

	# print(trie)
	# print(text)

	v = trie[0]

	for i in range(len(text)):
		if prefix_matching(text[i:], trie):
			result.append(i)

	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
