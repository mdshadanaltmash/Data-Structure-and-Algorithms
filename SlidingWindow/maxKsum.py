
def maxSumWithFixedWindow(arr, k):
    max_window_sum=curr_window_sum = sum([arr[i] for i in range(k)])
    for i in range(len(arr)-k):
        curr_window_sum = curr_window_sum -arr[i]+arr[i+k]
        max_window_sum = max(curr_window_sum, max_window_sum)

    return(max_window_sum)

arr = [400,40,-40,50,300,100,20,200,80]
k=2
print(maxSumWithFixedWindow(arr, k))