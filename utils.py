from collections import deque

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.checked = False
        self.children = []

    def insert_child(self, node):
        self.children.append(node)


qu = deque()

root = Node("root", 5)
n = Node("n", 10)
a = Node("a", 12)
c = Node("c", 20)
e = Node("e", 123)
root.insert_child(n)
n.insert_child(a)
root.insert_child(c)
a.insert_child(e)


def dfs(root_):
    print(root_)
    q = deque([root_])
    while q:
        curr = q.popleft()
        for child in curr.children:
            q.append(child)
            print(child.name)


def bubble_sort(list_):
    list_sorted = False
    while not list_sorted:
        results = []
        for i in range(len(list_) - 1):
            l1 = list_[i]
            l2 = list_[i + 1]
            order = l1 < l2
            if not order:
                list_[i] = l2
                list_[i + 1] = l1
                results.append(False)
            else:
                results.append(True)
        if all(results):
            list_sorted = True