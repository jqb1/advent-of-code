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


def bfs(root_):
    print(root_)
    q = deque([root_])
    while q:
        curr = q.popleft()
        for child in curr.children:
            q.append(child)
            print(child.name)
