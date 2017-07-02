# python3
#from collections import deque

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.maxHeight = 0

    def compute_height(self):

        nodes = {}

        root = 0

        for i in range(self.n):
            nodes[i] = []

        for i in range(self.n):
            if self.parent[i] == -1:
                root = i
            else:
                nodes[self.parent[i]].append(i)

        # count DFS
        # def print_node(node, h):
        #
        #     h += 1
        #
        #     self.maxHeight = max(self.maxHeight, h)
        #
        #     for i in range(len(node)):
        #       print_node(nodes[node[i]], h)
        # print_node(nodes[root], 0)


        # count BFS

        def print_node(parent):

            self.maxHeight += 1

            #print('parent', parent)

            childs = []

            while len(parent) > 0:

                node = nodes[parent.pop()]

                if len(node) > 0:

                    for i in node:
                        childs.append(i)

            #print('childs', childs)

            if len(childs) > 0:

                print_node(childs)

        print_node([root])

        return self.maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
