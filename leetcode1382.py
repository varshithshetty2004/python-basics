# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):  # ← FIXED: double underscores
        self.values = []

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.values.append(root.val)
        self.inorder(root.right)

    def createBST(self, values, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(values[mid])
        node.left = self.createBST(values, left, mid - 1)
        node.right = self.createBST(values, mid + 1, right)
        return node

    def balanceBST(self, root):
        self.inorder(root)
        return self.createBST(self.values, 0, len(self.values) - 1)
