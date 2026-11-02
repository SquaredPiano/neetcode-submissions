# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curr_index = 1
        self.tree_val = None
        def dfs(tree):
            if not tree or self.tree_val is not None:
                return
            
            dfs(tree.left)
            if self.curr_index == k:
                self.tree_val = tree.val
            self.curr_index += 1
            dfs(tree.right)
        dfs(root)
        return self.tree_val