# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Node:
    def __init__(self, key=None):
        self.key = key
        self.child_list = []


class TreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = None
        self.nodes_array = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def create_array_nodes(self):
        for i in range(self.n):
            node = Node(i)
            self.nodes_array.append(node)

    def compute_height(self):
        # Replace this code with a faster implementation
        max_height = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            max_height = max(max_height, height)
        return max_height


def main():
    tree = TreeHeight()
    tree.read()
    tree.create_array_nodes()
    print(tree.compute_height())
    threading.Thread(target=main).start()



