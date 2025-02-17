"""
Given an array arr[] of integers, the task is to find the Next Greater Element for each element of the array in order of their appearance in the array.
Note: The Next Greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1.

Examples:

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn’t exist, it is -1.


Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on right and hence -1.


Input: arr[] = [50, 40, 30, 10]
Output: [-1, -1, -1, -1]
Explanation: There is no greater element for any of the elements in the array, so all are -1.

link: https://www.geeksforgeeks.org/next-greater-element/
"""


def next_greater_elem(arr: [list[int]]) -> list[int]:
    res = []
    for i in range(len(arr)):
        found = False
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                res.append(arr[j])
                found = True
                break
        if not found:
            res.append(-1)

    return res


def next_greater_elem_optimised(arr: [list[int]]) -> list[int]:
    n = len(arr) - 1
    res = [-1] * (n+1)
    stack = []
    for num in reversed(arr):
        while stack and num >= stack[-1]:
            stack.pop()
        if stack:
            res[n] = stack[-1]
        stack.append(num)
        n -= 1
    return res


lst = [41, 88, 58, 69, 93, 42, 44, 25, 12, 47, 41, 88, 58, 69, 93, 42, 44, 25, 12, 47]
print(next_greater_elem(lst))
print(next_greater_elem_optimised(lst))
