from Array.maximum_subarray_sum import max_sub_array_sum_kadane
from Array.min_subarray_sum import min_subarray_sum_kadane


def max_circular_subarray_sum(arr):
    max_sub_arr_sum = max_sub_array_sum_kadane(arr)
    min_sub_arr_sum = min_subarray_sum_kadane(arr)
    arr_total_sum = sum(arr)

    return max(max_sub_arr_sum, arr_total_sum-min_sub_arr_sum)


lst = [34, -50, 42, 14, -5, 86]
print(max_circular_subarray_sum(lst))
