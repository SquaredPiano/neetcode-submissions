# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #  1
        #   2
        #  3 4
        # 5
        # 5 should return 0, 0
        # 3 should return 1, 1
        # 4 should return 0, 0
        # 2 should return 2, 2
        # 1 should return 3, 3

        #  1
        # 2 3
        # 2 should return 0, 0
        # 3 should return 0, 0
        # 1 should return 1, 2
        def dfs(tree) -> tuple[int, int]:
            if tree is None:
                return None, 0
            elif tree.left is None and tree.right is None:
                return 0, 0
            depthLeft, diameterLeft = dfs(tree.left)
            depthRight, diameterRight = dfs(tree.right)
            if depthRight is None:
                depth = 1 + depthLeft
                diam = depth
            elif depthLeft is None:
                depth = 1 + depthRight
                diam = depth
            else:
                depth = 1 + max(depthLeft, depthRight)
                diam = 2 + depthLeft + depthRight
            return depth, max(diameterLeft, diameterRight, diam)
            
        return dfs(root)[1]