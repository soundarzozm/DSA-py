from binary_tree import Node, BinaryTree
from typing import Optional

class Solution:
    def countNodes(self, root: Optional[Node]) -> int:
        # Base case - if node does not exist we cannot count it so it is 0
        if not root:
            return 0

        # Find the height of the leftmost and the rightmost nodes of the current subtree
        # If the heights are equal, it is a complete subtree. So we don't have to traverse it further
        leftHeight = self.findLeftHeight(root)
        rightHeight = self.findRightHeight(root)

        if leftHeight == rightHeight:
            return (2**leftHeight) - 1

        # If the heights are not equal, it means the subtree is not complete
        # So we traverse further inside and process the smaller complete subtrees
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def findLeftHeight(self, node):
        # This method returns the height of the leftmost leaf of the current subtree
        leftHeight = 0

        while node:
            leftHeight += 1
            node = node.left

        return leftHeight

    def findRightHeight(self, node):
        # This method returns the height of the rightmost leaf of the current subtree
        rightHeight = 0

        while node:
            rightHeight += 1
            node = node.right

        return rightHeight

if __name__ == "__main__":
    solution = Solution()
    preorder = [1,2,3,4,5,6]
    rootNode = BinaryTree().createFromPreorder(preorder)
    print(solution.countNodes(rootNode))
