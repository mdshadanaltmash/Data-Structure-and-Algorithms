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

array = [1,2,4,7,9,12,14,17,18]
print(linear_search(array,9))
print(binary_search(array, 14))