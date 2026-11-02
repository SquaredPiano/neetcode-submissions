class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        ROWS = "rows"
        COLS = "cols"
        BOXES = "boxes"
        sets = {}

        for i in range(n):
            if not ROWS in sets:
                sets[ROWS] = {}
            if not COLS in sets:
                sets[COLS] = {}
            if not BOXES in sets:
                sets[BOXES] = {}
            
            sets[ROWS][i] = set()
            sets[COLS][i] = set()
            sets[BOXES][i] = set()
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in sets[ROWS][i]:
                    return False
                elif board[i][j] in sets[COLS][j]:
                    return False
                elif board[i][j] in sets[BOXES][(i // 3) * 3 + (j // 3)]:
                    return False
                
                sets[ROWS][i].add(board[i][j])
                sets[COLS][j].add(board[i][j])
                sets[BOXES][(i // 3) * 3 + (j // 3)].add(board[i][j])
        
        return True