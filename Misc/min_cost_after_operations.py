"""
Given an array of n integers. We need to reduce size of array to one. We are allowed to select a pair
of integers and remove the larger one of these two. This decreases the array size by 1.
Cost of this operation is equal to value of smaller one. Find out minimum sum of costs of operations
needed to convert the array into a single element.

Examples:

Input: 4 3 2
Output: 4
Explanation: Choose (4, 2) so 4 is removed, new array = {2, 3}. Now choose (2, 3) so 3 is removed.
So total cost = 2 + 2
"""

arr = [4, 3, 2]
arr.sort()
cost = 0
for i in range(1, len(arr)):
    cost += arr[0]
print(cost)
# O(n*logn)

# prefix difference?????