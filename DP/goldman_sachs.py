
# Complete the nonRepeatingDigitProductCount function below.
def nonRepeatingDigitProductCount(x, y, z):
    count = 0
    for num in range(y, z+1):
        curr_num = x * num
        digits1 = get_digits(num)
        digits2 = get_digits(curr_num)
        for d in digits2:
            if d in digits1:
                break
        else:
            count += 1
    return count

def get_digits(n):
    digits = set()
    while n >= 0:
        digits.add(n%10)
        n = n // 10
    return digits

print(nonRepeatingDigitProductCount(1, 0, 99))

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
