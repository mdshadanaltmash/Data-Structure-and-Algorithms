def flatten(arr):
    arr_n = []
    if isinstance(arr[0]) !='List':
        return arr[0]
    else:
        return arr_n.append(arr[0])




print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]