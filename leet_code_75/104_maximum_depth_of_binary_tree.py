from extra.tree_node import add, preorder, height

if __name__ == "__main__":
    data = [9, 3, 20, 15, 7]
    root = None
    
    for d in data:
        root = add(root, d)

    preorder(root)
    h = height(root)
    print(h)
