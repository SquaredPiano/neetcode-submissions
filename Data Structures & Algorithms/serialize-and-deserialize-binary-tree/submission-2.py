from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            curr_node, depth = q.popleft()
            if not curr_node:
                res.append("N")
            else:
                res.append(curr_node.val)
                q.append((curr_node.left, depth + 1))
                q.append((curr_node.right, depth + 1))
        return "|".join(str(item) for item in res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        bfs_lst = data.split("|")
        for i, item in enumerate(bfs_lst):
            if item != "N":
                bfs_lst[i] = int(item)
        q = deque()
        root = TreeNode(bfs_lst[0])
        q.append(root)
        bfs_lst_pointer = 1
        while q:
            node = q.popleft()
            left = bfs_lst[bfs_lst_pointer]
            right = bfs_lst[bfs_lst_pointer + 1]
            bfs_lst_pointer += 2
            if left == "N":
                node.left = None
            else:
                node.left = TreeNode(left)
                q.append(node.left)
            if right == "N":
                node.right = None
            else:
                node.right = TreeNode(right)
                q.append(node.right)

        return root