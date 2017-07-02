# python3
import sys

def build_trie(patterns):

	# for p in patterns:
	#     print(p)

	# init root node
	tree = dict()

	nodes = 1

	last_node = None

	for p in patterns:

		current_node = 0

		last = 0

		for i in range(len(p)):

			last = current_node

			if current_node not in tree:
				tree[current_node] = {}

			# print(tree)

			if p[i] in tree[current_node]:
				current_node, _ = tree[current_node][p[i]]
			else:
				tree[current_node][p[i]] = (nodes, 0)
				current_node = nodes
				nodes += 1

			if i == len(p) - 1:
				# print(tree[last], p[i])
				tree[last][p[i]] = (tree[last][p[i]][0] , 1)

	# for node in tree:
	#     print(node, tree[node])

	return tree

def prefix_matching(text, trie):
	# print(text)

	v = trie[0]

	for i in range(len(text)):
		if text[i] in v:

			nxt, is_match =  v[text[i]]

			if is_match:
				return True

			if nxt in trie:
				v = trie[nxt]
			else:
				return True
		else:
			return False

	# if v['$']:
	# 	return True
	# else:
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
