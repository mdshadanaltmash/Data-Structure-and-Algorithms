"""
Given an integer array, the task is to find the maximum product of any subarray.

Examples:

Input: arr[] = {-2, 6, -3, -10, 0, 2}
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180


Input: arr[] = {-1, -3, -10, 0, 60}
Output: 60
Explanation: The subarray with maximum product is {60}.
"""

"""
a * 1
a * b
a *(-b)
a * 0
"""

arr = [-2, 6, -3, -10, 0, 2]
arr = [-1, -3, -10, 0, 6]
curr_prod = prev_prod = max_prod = arr[0]
for i in range(1, len(arr)):
    prev_prod = curr_prod
    if curr_prod * arr[i] == 0:
        curr_prod = 1
    curr_prod *= arr[i]

    max_prod = max(max_prod, prev_prod, curr_prod, arr[i])

print(max_prod)  # wrong

curr_min_prod = curr_max_prod = max_prod = arr[0]

for i in range(1, len(arr)):
    temp = max(arr[i], arr[i] * curr_max_prod, arr[i] * curr_min_prod)
    curr_min_prod = min(arr[i], arr[i] * curr_max_prod, arr[i] * curr_min_prod)
    curr_max_prod = temp
    max_prod = max(max_prod, curr_max_prod)
print(max_prod)
