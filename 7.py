from collections import defaultdict


def read_input():
    with open("/Users/jkoziol/Downloads/input.txt") as f:
        moves = [line.rstrip() for line in f]
    return moves


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = defaultdict(Dir)
        self.data = []
        self.size = 0

    def insert_child(self, dir_):
        self.children[dir_.name] = dir_

    def get_child(self, name):
        return self.children[name]

    def insert_file(self, size):
        self.size += size


def inorder_search_sizes(dir_):
    for name, child in dir_.children.items():
        inorder_search_sizes(child)
    dir_.size += sum(child.size for _, child in dir_.children.items())
    sizes.append(dir_.size)


sizes = []

root = Dir("/", None)
current_dir = root
for terminal in read_input():
    if terminal == '$ cd /':
        current_dir = root
        continue
    if terminal.startswith("$"):
        if terminal.split()[1] == "cd":
            dir_name = terminal.split()[2]
            current_dir = current_dir.parent if dir_name == ".." else current_dir.get_child(dir_name)
    else:
        info, name_ = terminal.split()
        if info == "dir":
            current_dir.insert_child(Dir(name_, current_dir))
        else:
            current_dir.insert_file(int(info))

max_size = 100000
inorder_search_sizes(root)
print("sum is")
print(sum(s if s <= max_size else 0 for s in sizes))

# =========================== part2 ===========================

total = 70000000
used = root.size
unused = total - used
required = 30000000

to_be_freed = required - unused
for s in sorted(sizes):
    if s >= to_be_freed:
        print(s)
        break
