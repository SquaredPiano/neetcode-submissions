# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_indices = {}
        for i, node in enumerate(inorder):
            inorder_indices[node] = i
        self.pre_index = 0
        def dfs(preorder, inorder, l, r):
            if l > r:
                return
            
            root = TreeNode(preorder[self.pre_index])
            mid = inorder_indices[root.val]
            self.pre_index += 1

            root.left = dfs(preorder, inorder, l, mid-1)
            root.right = dfs(preorder, inorder, mid+1, r)
            
            return root
        
        return dfs(preorder, inorder, 0, len(preorder)-1)