"""
You are given an array of n-elements, you have to find the number of operations needed to make all
elements of array equal. Where a single operation can increment an element by k. If it is not possible to
make all elements equal print -1.

Example :

Input : arr[] = {4, 7, 19, 16},  k = 3
Output : 10

Input : arr[] = {4, 4, 4, 4}, k = 3
Output : 0

Input : arr[] = {4, 2, 6, 8}, k = 3
Output : -1
"""

arr = [4, 2, 6, 8]
k = 3


def get_no_of_operation(arr, k):
    cnt = 0
    max_elem = max(arr)
    for i in range(len(arr)):
        while arr[i] < max_elem:
            arr[i] += k
            cnt += 1
        if arr[i] > max_elem:
            return -1
    return cnt


print(get_no_of_operation(arr, k))


def get_no_of_operation_optimized(arr, k):
    cnt = 0
    max_elem = max(arr)
    for i in range(len(arr)):
        if (max_elem - arr[i]) % k != 0:
            return -1
        else:
            cnt += ((max_elem - arr[i]) / k)
