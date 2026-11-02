# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total_count = 0
        def dfs(tree, geq_val):
            if not tree:
                return # TODO return value
        
            if tree.val >= geq_val:
                geq_val = tree.val
                self.total_count += 1
            dfs(tree.left, geq_val)
            dfs(tree.right, geq_val)
            return # TODO return value
        dfs(root, root.val)
        return self.total_count