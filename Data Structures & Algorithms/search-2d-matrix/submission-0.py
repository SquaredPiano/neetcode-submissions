class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        lo = 0
        hi = n * m

        # to get plain int from
        # raw row, col,
        # we do index = m * row + col
        # to get reverse:
        # (index - col)/m = row
        while lo < hi:
            mid = (lo + hi) // 2
            matrix_val = matrix[mid // m][mid % m]
            if matrix_val == target:
                return True
            elif matrix_val < target:
                lo = mid + 1
            else:
                hi = mid
        return False