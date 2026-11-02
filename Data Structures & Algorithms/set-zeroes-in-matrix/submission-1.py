class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        def r_c(i, j):
            for a in range(m):
                if matrix[i][a] is not None:
                    matrix[i][a] = 0
            
            for b in range(n):
                if matrix[b][j] is not None:
                    matrix[b][j] = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = None

        for i in range(n):
            for j in range(m):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
                    r_c(i, j)
        