def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] =arr[j+1], arr[j]
    print(arr)

input_arr = [6,1,2,5,4,9,8,7,3]
bubble_sort(input_arr)