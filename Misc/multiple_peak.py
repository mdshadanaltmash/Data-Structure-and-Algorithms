"""
Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak element if it is strictly greater than its adjacent elements. If there are multiple peak elements, return the index of any one of them.

Note: Consider the element before the first element and the element after the last element to be negative infinity.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 5
Explanation: arr[5] = 8 is a peak element because arr[
8 is a peak element because arr[4] < arr[5] > arr[6].


Input: arr[] = [10, 20, 15, 2, 23, 90, 80]
Output: 1 or 5
Explanation: arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] < arr[1] > arr[2] and arr[4] < arr[5] > arr[6].


Input: arr[] = [1, 2, 3]
Output: 2
Explanation: arr[2] is a peak element because arr[1] < arr[2] and arr[2] is the last element, so it has negative infinity to its right.
"""

arr = [1, 2, 4, 5, 7, 8, 3]
i = 0
idxs = []
if len(arr) == 1:
    print([0])
while i < len(arr):
    if ((i == 0 and arr[i] > arr[i + 1])
            or (i == len(arr) - 1 and arr[i] > arr[i - 1])
            or (arr[i - 1] < arr[i] > arr[i + 1])):
        idxs.append(i)
    i += 1
print(idxs)


def find_one_peak(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    lo, hi = 1, n - 2

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] > arr[mid - 1]:
            lo = mid + 1
        else:
            hi = mid - 1


print(find_one_peak(arr))
