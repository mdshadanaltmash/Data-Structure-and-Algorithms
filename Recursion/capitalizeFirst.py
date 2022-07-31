def capitalizeFirst(arr):
    arr_n = []
    if len(arr)==0:
        return arr_n
    else:
        result = arr_n.append(arr[0].capitalize())
    return arr_n + capitalizeFirst(arr[1:])


print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana'])