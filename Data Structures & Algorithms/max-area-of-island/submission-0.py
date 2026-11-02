from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            while q:
                r, c = q.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r+dr][c++dc] == 1:
                        q.append((r + dr, c + dc))

        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if (r, c) not in visited:
                        prev_visited_len = len(visited)
                        bfs(r, c)
                        new_visited_len = len(visited)
                        result = max(result, new_visited_len - prev_visited_len)
        
        return result