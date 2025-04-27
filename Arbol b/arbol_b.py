
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = leaf

    def insert_non_full(self, k):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(0)
            while i >= 0 and k < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = k
        else:
            while i >= 0 and k < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if k > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(k)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.leaf:
            self.children[-1].traverse()

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == k:
            return True
        if self.leaf:
            return False
        return self.children[i].search(k)

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, True)

    def insert(self, k):
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t, False)
            s.children.insert(0, r)
            s.split_child(0)
            i = 0
            if s.keys[0] < k:
                i += 1
            s.children[i].insert_non_full(k)
            self.root = s
        else:
            r.insert_non_full(k)

    def search(self, k):
        return self.root.search(k)

    def to_graphviz(self):
        from graphviz import Digraph
        dot = Digraph()
        def add_nodes_edges(node, name="R"):
            label = "|".join(map(str, node.keys))
            dot.node(name, label, shape="record")
            for i, child in enumerate(node.children):
                child_name = f"{name}_{i}"
                add_nodes_edges(child, child_name)
                dot.edge(name, child_name)
        add_nodes_edges(self.root)
        return dot
