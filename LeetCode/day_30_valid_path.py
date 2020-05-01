"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is
a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the
nodes along a path results in a sequence in the given binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        def check(root, arr, i, l):

            if root is None:
                return l == 0

            if i == l - 1 and root.left is None and root.right is None and root.val == arr[i]:
                return True

            if i < l - 1 and root.val == arr[i]:
                return check(root.left, arr, i + 1, l) or check(root.right, arr, i + 1, l)
            return False

        return check(root, arr, 0, len(arr))
