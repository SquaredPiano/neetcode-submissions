# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree):
            if not tree:
                return 0, True
            
            leftHeight, leftIsBalanced = dfs(tree.left)
            rightHeight, rightIsBalanced = dfs(tree.right)
            isBalanced = leftIsBalanced and rightIsBalanced and abs(leftHeight - rightHeight) <= 1
            
            return 1 + max(leftHeight, rightHeight), isBalanced
            
        return dfs(root)[1]