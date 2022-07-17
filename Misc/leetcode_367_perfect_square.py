def isPerfectSquare(num: int) -> bool:
    i = 0
    j = num
    while i <= j:
        m = (i + j) // 2
        if m ** 2 == num:
            return True
        elif m ** 2 > num:
            j = m - 1
        else:
            i = m + 1
    return False

print(isPerfectSquare(17))