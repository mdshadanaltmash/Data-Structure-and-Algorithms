def find_smallest_window(arr):
    left = right = None
    s = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != s[i] and left is None:
            left = i
        elif arr[i] != s[i]:
            right = i
    return left, right


def find_smallest_window_optimized(arr):
    left = right = None
    max_seen, min_seen = float("-inf"), float("inf")
    n = len(arr)

    for i in range(n):
        max_seen = max(max_seen, arr[i])
        if arr[i] < max_seen:
            right = i

    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, arr[i])
        if arr[i] > min_seen:
            left = i

    return left, right


arr = [3, 7, 5, 6, 9]
print(find_smallest_window(arr))
print(find_smallest_window_optimized(arr))
