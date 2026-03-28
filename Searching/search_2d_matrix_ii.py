class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # finding column
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        for i in range(left):
            l1, r1 = 0, len(matrix[i]) - 1
            while l1 <= r1:
                mid1 = (l1 + r1) // 2
                if matrix[i][mid1] == target:
                    return True
                elif matrix[i][mid1] < target:
                    l1 = mid1 + 1
                else:
                    r1 = mid1 - 1
        return False


m = [[1, 4, 7, 11, 15],
     [2, 5, 8, 12, 19],
     [3, 6, 9, 16, 22],
     [10, 13, 14, 17, 24],
     [18, 21, 23, 26, 30]]


class Solution_internet:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        left, right = 0, n - 1

        while left < m and right >= 0:

            mid = matrix[left][right]

            if mid < target:
                left += 1
            elif mid > target:
                right -= 1
            else:
                return True

        return False


obj = Solution()
print(obj.searchMatrix(m, 5))
obj = Solution_internet()
print(obj.searchMatrix(m, 5))
