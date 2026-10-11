class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1 (0, 0) -> (0, 2)
        # 2 (0, 1) -> (1, 2)
        # 3 (0, 2) -> (2, 2)
        # 4 (1, 0) -> (0, 1)
        # 5 (1, 1) -> (1, 1)
        # 6 (1, 2) -> (2, 1)
        # 7 (2, 0) -> (0, 0)
        # 8 (2, 1) -> (1, 2)
        # 9 (2, 2) -> (2, 0)
        
        # 1 (0, 0) -> (0, 1)
        # 2 (0, 1) -> (1, 1)
        # 3 (1, 0) -> (0, 0)
        # 4 (1, 1) -> (1, 0)

        # 1 (0, 0) -> (0, 3)
        # 2 (0, 1) -> (1, 3)
        # 3 (0, 2) -> (2, 3)
        # 4 (0, 3) -> (3, 3)
        # 5 (1, 0) -> (0, 2)
        # 6 (1, 1) -> (1, 2)
        # 7 (1, 2) -> (2, 2)
        # 8 (1, 3) -> (3, 2)
        # 9 (2, 0) -> (0, 1)
        # 10 (2, 1) -> (1, 1)
        # 11 (2, 2) -> (2, 1)
        # 12 (2, 3) -> (3, 1)
        # 13 (3, 0) -> (0, 0)
        # 14 (3, 1) -> (1, 0)
        # 15 (3, 2) -> (2, 0)
        # 16 (3, 3) -> (3, 0)

        # row 0 becomes column n - 1
        # row 1 becomes column n - 2
        # and so on.

        # this is basically a matrix transpose
        # swap rows to columns
        # now 
        # but we need to then swap column i with columns (n - 1 - i)
        n = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]
