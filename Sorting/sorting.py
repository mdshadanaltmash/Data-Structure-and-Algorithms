def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] =arr[j+1], arr[j]
    print(arr)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    print(arr)

def insertion_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(0,min_index):
            if arr[i]<arr[j]:
                arr.insert(j,arr.pop(i))
    print(arr)


input_arr = [6,1,2,5,4,9,8,7,3,-1,0,10]
insertion_sort(input_arr)