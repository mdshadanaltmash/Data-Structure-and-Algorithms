def linear_search(arr, val) -> int:
    for i in range(len(arr)):
        if arr[i]==val:
            return i
    else:
        return -1

def binary_search(arr, val) -> int:
    start = 0
    end = len(arr)-1
    mid = (end+start)//2

    while not(arr[mid]==val) and start <= end:
        if arr[mid]<val:
            start = mid+1
        else:
            end = mid-1
        mid=(end+start)//2
    if arr[mid]==val:
        return mid
    else:
        return -1

def binary_search_recursion(arr, elt, left, right):
    if left>right:
            return False
    else:
        mid = (left+right)//2
        if arr[mid]==elt:
            return mid
        elif arr[mid]< elt:
            binary_search_recursion(arr,elt, mid+1, right)
        else: # arr[mid]<elt:
            binary_search_recursion(arr, elt, left, mid-1)

def b_search(arr, elt):
    a= binary_search_recursion(arr, elt, 0, len(arr)-1)
    return (a)
def leet_code(nums, target):
    start = 0
    end =len(nums)-1
    mid = (start+end)//2
    while not(nums[mid]==target) and start<end:
        if target<nums[mid]:
            end = mid
        else:
            start= mid+1
        mid =(start+end)//2
    if nums[mid]==target:
        return mid
    else:
        if target>nums[mid]:
            return mid+1
        else:
            return mid

data = [1,2,4,7,9,12,14,17,18]
#array=[1,3]
#print(linear_search(array,9))
print(b_search(data, 12))
#print(leet_code(array,0))