# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = root.val
        def dfs(tree):
            if not tree:
                return float('-inf')
            elif not tree.left and not tree.right:
                self.maxPathSum = max(self.maxPathSum, tree.val)
                return tree.val
            
            left = dfs(tree.left)
            right = dfs(tree.right)
            newPath = max(tree.val, tree.val + left, tree.val + right)
            
            self.maxPathSum = max(self.maxPathSum, tree.val, tree.val + left + right, tree.val + left, tree.val + right)
            return newPath
        dfs(root)
        return self.maxPathSum