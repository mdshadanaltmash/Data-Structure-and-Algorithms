def get_sum(n):
    if n==1:
        return 1
    return n + get_sum(n-1)

print(get_sum(11))

