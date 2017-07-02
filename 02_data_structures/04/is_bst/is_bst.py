#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size


def IsBinarySearchTree(key, left, right):

    arr = []

    prev = None

    def is_bst(i):

        #print(i, key[i], arr[-1:], left[i])

        if left[i] != -1:
            if key[i] == key[left[i]]:
                return False
            if not is_bst(left[i]):
                return False

        if len(arr):
            if key[i] < arr.pop():
                return False

        arr.append(key[i])

        if right[i] != -1:
            return is_bst(right[i])

        return True

    return is_bst(0)


def main():
  n = int(sys.stdin.readline().strip())
  key = [0 for i in range(n)]
  left = [0 for i in range(n)]
  right = [0 for i in range(n)]
  for i in range(n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      key[i] = a
      left[i] = b
      right[i] = c
    #tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if n == 0 or IsBinarySearchTree(key, left, right):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
