"""
Given array of integer, find the next smaller of next greater element of every element in array.


Note : Elements for which no greater element exists or no smaller of greater element exist, print -1.

Examples:

Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
Output:          2  2 -1  1 -1 -1 -1
Explanation :
Next Greater ->      Right Smaller
   5 ->  9             9 ->  2
   1 ->  9             9 ->  2
   9 -> -1            -1 -> -1
   2 ->  5             5 ->  1
   5 ->  7             7 -> -1
   1 ->  7             7 -> -1
   7 -> -1            -1 -> -1

Input  : arr[] = {4, 8, 2, 1, 9, 5, 6, 3}
Output :          2  5  5  5 -1  3 -1 -1

Link: https://www.geeksforgeeks.org/find-next-smaller-next-greater-array/
"""


def next_greaters_smaller_elem(arr: list[int]) -> list[int]:
    n = len(arr)
    res = []

    for i in range(n):
        next = -1
        flag = False
        ans = -1
        
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                next = j
                break
        if next == -1:
            res.append(-1)
        else:
            for k in range(next+1, n):
                if arr[k] < arr[next]:
                    res.append(arr[k])
                    flag = True
                    break
            if not flag:
                res.append(-1)
    return res


# def next_greaters_smaller_elem_optimised(arr: list[int]) -> list[int]:
#     n = len(arr)
#     res = [-1] * n
#     stack_inc = []
#
#     for i in range(n-1, -1, -1):
#         k = i
#         while stack_inc and stack_inc[-1] <= arr[i]:
#             stack_inc.pop()
#         if not stack_inc:
#             stack_inc.append(i)


lst = [4, 8, 2, 1, 9, 5, 6, 3]
print(next_greaters_smaller_elem(lst))
