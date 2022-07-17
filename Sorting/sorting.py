import math
import random

def bubble_sort(arr):
    print("Using Bubble sort")
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] =arr[j+1], arr[j]
    return(arr)

def selection_sort(arr):
    print("Using Selection sort")
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return (arr)

def insertion_sort(arr):
    print("Using Insertion sort")
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return(arr)

def insertion_sort_with_binary_search(arr):
    print("Using insertion_sort_with_binary_search")
    for i in range(1,len(arr)):
        start = 0
        end =i-1
        mid = (start+end)//2
        while start<end:
            if arr[i]<arr[mid]:
                end = mid
            else:
                start= mid+1
            mid = (start+end)//2
        if arr[i]>arr[mid]:
            arr.insert(mid+1,arr.pop(i))
        else:
            arr.insert(mid,arr.pop(i))
    return(arr)

def merge_sort(arr):
    size = len(arr)
    if size > 1:
        middle_end = size//2
        l = arr[:middle_end]
        r = arr[middle_end:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        l_size = len(l)
        r_size = len(r)
        while i<l_size and j<r_size:
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else: 
                arr[k] = r[j]
                j+=1
            k+=1
        while i < l_size:
            arr[k] = l[i]
            k+=1
            i+=1
        while j < r_size:
            arr[k] = r[j]
            k+=1
            j+=1
    return arr

def bucket_sort(arr_list):
    #does not work for 0 and negative number
    no_of_buckets = round(math.sqrt(len(arr_list)))
    max_value = max(arr_list)
    total_buckets = []

    #creating buckets
    for i in range(no_of_buckets):
        total_buckets.append([])
    
    #inserting each value in appropriate bucket
    for j in arr_list:
        bucket_no = math.ceil((j*no_of_buckets)/max_value)
        total_buckets[bucket_no-1].append(j)

    #sorting Buckets
    list_of_sorting = [merge_sort,bubble_sort, selection_sort, insertion_sort, insertion_sort_with_binary_search]
    for i in range(no_of_buckets):
        
        total_buckets[i] = random.choice(list_of_sorting)(total_buckets[i])
    
    #merging Buckets
    k = 0
    for i in range(no_of_buckets):
        for j in range(len(total_buckets[i])):
            arr_list[k] = total_buckets[i][j]
            k+=1
    return(arr_list)

 
inp_arr = [11, 31, 7, 41, 101, 56, 77, 2]
print("Input Array:\n")
print(inp_arr)
merge_sort(inp_arr)
print("Sorted Array:\n")
print(inp_arr)
#arr = [6,1,2,5,4,9,8,7,3,10]
arr = [-2,3,-5]
print(merge_sort(arr))