class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        r = m * n - 1
        l = 0

        while (l <= r):
            mid = l + (r - l) // 2

            i = mid % n
            j = mid // n

            if (matrix[j][i] < target):
                l = mid + 1
            elif (matrix[j][i] > target):
                r = mid - 1
            else:
                return True
    
        return False
            

