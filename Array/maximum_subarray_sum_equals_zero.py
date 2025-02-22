#GOLDMAN SACHS Interview

# /*Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
# Examples
# Example 1:
# Input Format
# : N = 6, array[] = {9, -3, 3, -1, 6, -5}
# max_len=5
# Result
# : 5
# Explanation
# : The following subarrays sum to zero:
# {-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
# Since we require the length of the longest subarray, our answer is 5!
# Example 2:
# Input Format:
#  N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}
# Result
# : 8
# Subarrays with sum 0 : {-2, 2}, {-8, 1, 7}, {-2, 2, -8, 1, 7}, {6, -2, 2, -8, 1, 7, 4, -10}
# # Length of longest subarray = 8
# # Example 3:
# # Input Format:
# #  N = 3, array[] = {1, 0, -5}
# # Result
# # : 1
# # Subarray : {0}
# # Length of longest subarray = 1
# # Example 4:
# # Input Format:
# #  N = 5, array[] = {1, 3, -5, 6, -2}
# # Result
# # : 0
# # Subarray: There is no subarray that sums to zero
# # */

# # //{9, -3, 3, 1, 6, 5}

def max_sum_zero_len(arr):
    prefix_map = dict()
    curr_sum = 0
    max_len = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0:
            max_len = i + 1
        if curr_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[curr_sum])
        else:
            prefix_map[curr_sum] = i
    return max_len


lst = [1, 0, -1]
print(max_sum_zero_len(lst))
#
# 1: 0
# 0

