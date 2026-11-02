from collections import deque, defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        map = {}
        def dfs(curr_node):
            if curr_node.val in map:
                return map[curr_node.val]
            new_node = Node(curr_node.val)
            map[curr_node.val] = new_node

            for nei in curr_node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node
        
        return dfs(node)