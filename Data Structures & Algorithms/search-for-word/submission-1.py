from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        q = deque()
        word_split = list(word)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    q.append((i, j, [board[i][j]]))
        
        def dfs(i, j, path, visited):
            if len(path) == len(word_split):
                if path == word_split:
                    return True
            
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]) and (i + di, j + dj) not in visited and board[i + di][j + dj] == word_split[len(path)]:
                    visited.add((i + di, j + dj))
                    if dfs(i + di, j + dj, path + [board[i + di][j + dj]], visited):
                        return True
                    visited.remove((i + di, j + dj))
            
        for item in q:
            x, y, letter = item
            if dfs(x, y, letter, {(x, y)}):
                return True
        
        return False