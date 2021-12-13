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
    list_of_sorting = [bubble_sort, selection_sort, insertion_sort, insertion_sort_with_binary_search]
    for i in range(no_of_buckets):
        
        total_buckets[i] = random.choice(list_of_sorting)(total_buckets[i])
    
    #merging Buckets
    k = 0
    for i in range(no_of_buckets):
        for j in range(len(total_buckets[i])):
            arr_list[k] = total_buckets[i][j]
            k+=1
    return(arr_list)


input_arr = [6,1,2,5,4,9,8,7,3,10]
print(bucket_sort(input_arr))