def linear_search(arr, val) -> int:
    for i in range(len(arr)):
        if arr[i]==val:
            return i
    else:
        return -1
        
array = [1,2,4,7,9,12,14,17,18]
print(linear_search(array,9))