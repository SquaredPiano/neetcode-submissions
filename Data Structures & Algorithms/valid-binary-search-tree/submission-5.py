# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree, ge_val=float('-inf'), le_val=float('inf')):
            if tree is None:
                return True
            if ge_val < tree.val < le_val:
                return dfs(tree.left, ge_val, tree.val) and dfs(tree.right, tree.val, le_val)
            return False
            
        return dfs(root)