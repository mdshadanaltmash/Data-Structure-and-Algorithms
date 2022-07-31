def flatten(arr):
    arr_n = []
    for custItem in arr:
        if isinstance(custItem,list):
            arr_n.extend(flatten(custItem))
        else:
            arr_n.append(custItem)
    return arr_n



print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]