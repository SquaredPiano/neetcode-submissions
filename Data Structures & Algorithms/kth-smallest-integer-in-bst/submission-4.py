# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curr_index = 1
        def dfs(tree):
            if not tree:
                return
            
            if (res := dfs(tree.left)) is not None: return res
            if self.curr_index == k:
                return tree.val
            self.curr_index += 1
            return dfs(tree.right)
        return dfs(root)