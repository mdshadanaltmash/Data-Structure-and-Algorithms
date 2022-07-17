import time
def array_inversion(arr):
    temp_arr = [-1]*len(arr)
    return count_inversion(arr, temp_arr, 0, len(arr)-1)

def count_inversion(arr, temp_arr, left, right):
    inv_count = 0
    if left<right:
        mid =(left+right)//2
        inv_count += count_inversion(arr, temp_arr, left, mid)
        inv_count += count_inversion(arr, temp_arr, mid+1, right)
        inv_count += merge_and_count_inv(arr, temp_arr, left, mid, right)
    return inv_count

def merge_and_count_inv(arr, temp_arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    c_inv = 0

    while i<= mid and j <= right:
        if arr[i]<= arr[j]:
            temp_arr[k] = arr[i]
            i+=1
            k+=1
        else:
            temp_arr[k]= arr[j]
            j+=1
            k+=1
            c_inv+=(mid-i+1)
    
    while i<= mid:
        temp_arr[k]= arr[i]
        i+=1
        k+=1
    
    while j<= right:
        temp_arr[k] = arr[j]
        j+=1
        k+=1

    for x in range(left, right+1):
        arr[x] = temp_arr[x]
    return c_inv

start_time= time.time()
arr = []
#arr = [1,20, 6, 4,5]

with open('Misc/numbers.txt') as numbers:
    for num in numbers:
        arr.append(int(num))
print(array_inversion(arr))
end_time = time.time()
print(round((end_time-start_time),3))