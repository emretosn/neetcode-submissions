class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        arr = 0
        
        while r >= l:
            m = l + (r - l) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                arr = m
                break
        else:
            return False
        
        l, r = 0, len(matrix[arr]) - 1
        while r >= l:
            m = l + (r - l) // 2
            if target > matrix[arr][m]:
                l = m + 1
            else:
                r = m - 1
            if target == matrix[arr][m]:
                return True
        return False