# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each
#  number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def sortedSquares(nums):
    start=0
    end = len(nums)-1
    arr = []
    while end>start:
        cur_start = nums[start]**2
        cur_end = nums[end]**2
        if cur_end>cur_start:
            arr.insert(0,cur_end)
            end-=1
        else:
            arr.insert(0,cur_start)
            start+=1
    arr.insert(0,nums[start]**2)
    return arr


array=[-4,-1,0,3,10]
print(sortedSquares(array))