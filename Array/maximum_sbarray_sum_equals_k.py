"""
Given an array arr[] of size n containing integers, the task is to find the length of the longest subarray having sum equal to the given value k.

Note: If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.


Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = 15 is [-5, 8, -14, 2, 4] of length 5.


Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].

LINK: https://www.geeksforgeeks.org/longest-sub-array-sum-k/
"""


def get_max_subarray_sum_equals_k_len(arr, k):
    prefix_sums = dict()
    max_len = curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == k:
            max_len = i+1
        elif (curr_sum - k) in prefix_sums:
            max_len = max(max_len, i - prefix_sums[curr_sum - k])

        if curr_sum not in prefix_sums:
            prefix_sums[curr_sum] = i
    return max_len


# lst = [-5, 8, -14, 2, 4, 12]
lst = [10, 5, 2, 7, 1, -10]
k = 25
print(get_max_subarray_sum_equals_k_len(lst, k))
