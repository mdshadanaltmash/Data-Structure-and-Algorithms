"""
Remove duplicates from Sorted Array
Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear
at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

Note: The elements after the distinct ones can be in any order and hold any value, as they don’t affect the result.

Examples:

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]
Explanation: All the elements are 2, So only keep one
Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
Output: [1, 2, 3, 4, 5]

Input: arr[] = [1, 2, 3]
Output: [1, 2, 3]
Explanation : No change as all elements are distinct.
"""

res = []
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
arr = [1, 2, 3, 7, 7, 7, 9, 88, 88]
# print([set(arr)])
res.append(arr[0])
i, j = 0, 1

while len(arr) > j > i:
    if arr[i] != arr[j]:
        res.append(arr[j])
        i = j
    j += 1

print(res)

while len(arr) > j > i:
    if arr[i] != arr[j]:
        # arr.append(arr[j])
        i = j
        j += 1
    else:
        arr.pop(j)

print(arr)
