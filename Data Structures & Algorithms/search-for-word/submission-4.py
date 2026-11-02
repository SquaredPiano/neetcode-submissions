class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k, visited):
            if k == len(word):
                return True
            
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]) and (i + di, j + dj) not in visited and board[i + di][j + dj] == word[k]:
                    visited.add((i + di, j + dj))
                    if dfs(i + di, j + dj, k + 1, visited):
                        return True
                    visited.remove((i + di, j + dj))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1, {(i, j)}):
                        return True
        
        

        return False