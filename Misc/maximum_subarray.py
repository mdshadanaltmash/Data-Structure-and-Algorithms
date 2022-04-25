from json.encoder import INFINITY

def maximum_subarray(arr, low, high):
    if low == high:
        return (low, high, arr[low])
    else:
        mid = (low + high)//2
        left_low, left_high, left_sum = maximum_subarray(arr, low, mid)
        right_low, right_high, right_sum = maximum_subarray(arr, mid+1, high)
        cross_low, cross_high, cross_sum = maximum_cross_subarray(arr, low, mid, high)

    if left_sum>= right_sum and left_sum>= cross_sum:
        return(left_low, left_high, left_sum)
    elif right_sum>= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return(cross_low, cross_high, cross_sum)


def maximum_cross_subarray(arr, low, mid, high):
    cross_left_sum = -INFINITY
    max_low = max_high = mid
    sum = 0
    for i in range(mid,low-1, -1):
        sum += arr[i]
        if sum>=cross_left_sum:
            cross_left_sum = sum
            max_low = i
    cross_right_sum = -INFINITY
    sum = 0 
    for j in range(mid+1,high+1):
        sum += arr[j]
        if sum>=cross_right_sum:
            cross_right_sum = sum
            max_high = j
    return (max_low, max_high, cross_left_sum + cross_right_sum )
    


#INDEX STARTS WITH 0
arr = [5,-10,120,-200, -20, 5, 40, 55]
print(maximum_subarray(arr, 0, len(arr)-1))