class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def add(node: TreeNode, val: int) -> TreeNode:
    if node is None:
        return TreeNode(val)
    else:
        if val < node.val:
            node.left = add(node.left, val)
        elif val > node.val:
            node.right = add(node.right, val)

    return node

def preorder(node: TreeNode) -> None:
    if node is not None:
        print(node.val, end=" ")
        preorder(node.left)
        preorder(node.right)

def height(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
        
def search(root: TreeNode, val: int) -> TreeNode | None:
    if not root:
        return None
    
    if root.val == val:
        return root
    
    if root.val > val:
        return search(root.left, val)
    
    return search(root.right, val)