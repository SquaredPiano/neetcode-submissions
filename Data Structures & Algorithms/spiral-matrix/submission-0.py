class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        res = []
        new_left = 0
        new_right = len(matrix[0]) - 1
        new_top = 0
        new_bottom = len(matrix) - 1
        direction = "R"
        while (new_top <= new_bottom and new_left <= new_right):
            if direction == "R":
                if j > new_right:
                    new_top += 1
                    direction = "D"
                    i += 1
                    j -= 1
                else:
                    res.append(matrix[i][j])
                    j += 1
            elif direction == "D":
                if i > new_bottom:
                    new_right -= 1
                    direction = "L"
                    j -= 1
                    i -= 1
                else:
                    res.append(matrix[i][j])
                    i += 1
            elif direction == "L":
                if j < new_left:
                    new_bottom -= 1
                    direction = "U"
                    i -= 1
                    j += 1
                else:
                    res.append(matrix[i][j])
                    j -= 1
            else:
                if i < new_top:
                    new_left += 1
                    direction = "R"
                    j += 1
                    i += 1
                else:
                    res.append(matrix[i][j])
                    i -= 1
        
        return res
