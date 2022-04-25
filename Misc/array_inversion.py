def array_inv(arr):
    temp_arr = [-1]*len(arr)
    return count_inv (arr, temp_arr, 0, len(arr)-1)


def count_inv(arr, temp_arr, left, right):
    inv_count = 0
    if left< right:
        mid = (left + right)//2
        inv_count += count_inv(arr, temp_arr, left, mid)
        inv_count += count_inv(arr,temp_arr, mid+1, right)
        inv_count += merge_and_count_inv(arr, temp_arr, left, mid, right)
    return inv_count

def merge_and_count_inv(arr, temp_arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    c_inv = 0
    
    while i <= mid and j <= right:
        if arr[i]<= arr[j]:
            temp_arr[k] == arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k] == arr[j]
            k+=1
            j+=1
            c_inv += (mid-i+1)
    
    while i <= mid:
        temp_arr[k] = arr[i]
        k+=1
        i+=1
    while j <= right:
        temp_arr[k] = arr[j]
        k+=1
        j+=1

    for loop_var in range(left, right ):
        arr[loop_var] = temp_arr[loop_var]

    return c_inv 

arr = [1, 20, 6, 4, 5]

print(array_inv(arr))