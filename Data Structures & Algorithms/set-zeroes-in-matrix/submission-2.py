class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        # (x, y) signifies we want to 0 fill row x, and 0 fill column y
        def r_c(i, j):
            # iterate over each column in a row
            # i.e., iterate over a row
            for a in range(m):
                # Case 1: Same row, but a different column
                if matrix[i][a] == (i, a):
                    matrix[i][a] = (None, a)
                # Case 2: Same row column already filled
                elif matrix[i][a] == (i, None):
                    matrix[i][a] = 0
                # Case 3: Filled row, but different column
                elif matrix[i][a] == (None, a):
                    matrix[i][a] = (None, a)
                else:
                    matrix[i][a] = 0
            
            # Iterate over each row in a column
            # i.e., iterate over the column
            for b in range(n):
                # Case 1: Same column, different row
                if matrix[b][j] == (b, j): 
                    matrix[b][j] = (b, None)
                # Case 2: Same column, row already filled
                elif matrix[b][j] == (None, j):
                    matrix[b][j] = 0
                # Case 3: Filled column, different row
                elif matrix[b][j] == (b, None):
                    matrix[b][j] = (b, None)
                else:
                    matrix[b][j] = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = (i, j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == (i, j) or matrix[i][j] == (None, j) or matrix[i][j] == (i, None):
                    matrix[i][j] = 0
                    r_c(i, j)
        