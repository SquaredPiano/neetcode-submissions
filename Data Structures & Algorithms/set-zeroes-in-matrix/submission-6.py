class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        def wipe_col(column):
            for row in range(n):
                matrix[row][column] = 0
        
        def wipe_row(row):
            for column in range(m):
                matrix[row][column] = 0

        if matrix[0][0] == 0:
            matrix[0][0] = [True, True, 0]
        else:
            matrix[0][0] = [False, False, matrix[0][0]]
        
        for j in range(1, m):
            matrix[0][j] = [False, matrix[0][j]]
            if matrix[0][j][1] == 0:
                matrix[0][j][0] = True
        for i in range(1, n):
            matrix[i][0] = [False, matrix[i][0]]
            if matrix[i][0][1] == 0:
                matrix[i][0][0] = True

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 or (isinstance(matrix[i][j], list) and matrix[i][j][-1] == 0):
                    if i != 0 and j != 0:
                        matrix[i][0][0] = True
                        matrix[0][j][0] = True
                    else:
                        if i == 0: # We're on the first row
                            matrix[0][0][0] = True
                        else:
                            matrix[i][0][0] = True
                        
                        if j == 0: # We're on the first column
                            matrix[0][0][1] = True
                        else:
                            matrix[0][j][0] = True

        for j in range(1, m):
            if matrix[0][j][0]:
                wipe_col(j)
            else:
                matrix[0][j] = matrix[0][j][1]
        for i in range(1, n):
            if matrix[i][0][0]:
                wipe_row(i)
            else:
                matrix[i][0] = matrix[i][0][1]
        if matrix[0][0][0] and matrix[0][0][1]:
            wipe_row(0)
            wipe_col(0)
        elif matrix[0][0][0]:
            wipe_row(0)
        elif matrix[0][0][1]:
            wipe_col(0)
        else:
            matrix[0][0] = matrix[0][0][2]
        