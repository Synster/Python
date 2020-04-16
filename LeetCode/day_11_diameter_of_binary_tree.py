"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        diameter of binary tree is the max of height of left + height of right, left diameter, right diameter
        """
        def height(root: TreeNode):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if root is None:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(left_height + right_height, left_diameter, right_diameter)
