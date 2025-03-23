def export_to_graphviz(node, filename="abb.dot"):
    with open(filename, "w") as f:
        f.write("digraph BST {\n")
        _write_graphviz(node, f)
        f.write("}\n")

def _write_graphviz(node, f):
    if node:
        if node.left:
            f.write(f'    "{node.key}" -> "{node.left.key}";\n')
            _write_graphviz(node.left, f)
        if node.right:
            f.write(f'    "{node.key}" -> "{node.right.key}";\n')
            _write_graphviz(node.right, f)
