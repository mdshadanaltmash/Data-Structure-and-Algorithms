# User function Template for python3

class Solution:
    def search(self, arr, key):
        # Complete this function
        pivot_idx = self.find_pivot_idx(arr)
        res_left = self.binary_search(arr[0:pivot_idx], key)
        if res_left != -1:
            return res_left
        res_right = self.binary_search(arr[pivot_idx::], key)
        if res_right != -1:
            return pivot_idx + res_right
        return -1

    def binary_search(self, arr, key):
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def find_pivot_idx(self, arr):
        lo = 0
        hi = len(arr) - 1

        if arr[lo] < arr[hi]:
            return lo

        while lo < hi:
            mid = (lo + hi) // 2

            if arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    A = [3, 5, 1, 2]
    k = 6
    ob = Solution()
    print(ob.search(A, k))
    print("~")
