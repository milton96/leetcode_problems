from extra.tree_node import add, preorder, search

if __name__ == "__main__":
    data = [4,2,7,1,3]
    root = None
    
    for d in data:
        root = add(root, d)

    preorder(root)
    print("\n")
    ans = search(root, 5)
    preorder(ans)