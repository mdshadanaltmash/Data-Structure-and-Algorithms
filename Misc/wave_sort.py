"""
Given an unsorted array of integers, sort the array into a wave array. An array arr[0..n-1] is sorted
in wave form if:
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80}
Explanation:
here you can see {10, 5, 6, 2, 20, 3, 100, 80} first element is larger than the second and the same
thing is repeated again and again. large element – small element-large element -small element and so on.
it can be small
"""

arr = [10, 5, 6, 3, 2, 20, 100, 80]
arr.sort()

for i in range(0, len(arr) - 1, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)
# dharam ka call tha, dusra email id maang rha tha, taaki interview schedule ho jaaye

arr = [10, 5, 6, 3, 2, 20, 100, 80]
for i in range(0, len(arr) - 1, 2):
    j = i + 1
    while j < len(arr):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
print(arr)
