class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        ROWS = "rows"
        COLS = "cols"
        BOXES = "boxes"
        sets = {}

        def findBox(x, y):
            if 0 <= x < 3 and 0 <= y < 3:
                return 0
            elif 3 <= x < 6 and 0 <= y < 3:
                return 1
            elif 6 <= x < n and 0 <= y < 3:
                return 2
            if 0 <= x < 3 and 3 <= y < 6:
                return 3
            if 3 <= x < 6 and 3 <= y < 6:
                return 4
            if 6 <= x < n and 3 <= y < 6:
                return 5
            if 0 <= x < 3 and 6 <= y < n:
                return 6
            if 3 <= x < 6 and 6 <= y < n:
                return 7
            if 6 <= x < n and 6 <= y < n:
                return 8

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
                elif board[i][j] in sets[BOXES][findBox(j, i)]:
                    return False
                
                sets[ROWS][i].add(board[i][j])
                sets[COLS][j].add(board[i][j])
                sets[BOXES][findBox(j, i)].add(board[i][j])
        
        return True