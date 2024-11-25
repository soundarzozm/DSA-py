class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None
    
class BinaryTree:
    def createFromPreorder(self, preorder):
        if not preorder:
            return None
        root = Node(preorder[0])
        i = 1
        while i<len(preorder) and  preorder[i] < root.val:
            i+=1
        root.left = self.createFromPreorder(preorder[1:i])
        root.right = self.createFromPreorder(preorder[i:])
        return root