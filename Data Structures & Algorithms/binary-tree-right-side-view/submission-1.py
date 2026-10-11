from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            curr_node, depth = q.popleft()
            if len(res) != depth + 1:
                res.append([])
            res[depth] = curr_node.val
            if curr_node.left:
                q.append((curr_node.left, depth + 1))
            if curr_node.right:
                q.append((curr_node.right, depth + 1))
        
        return res