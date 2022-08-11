def isPowerOfTwo( n):
    if n == 0:
        return False
    elif n == 1:
        return True
    elif int(n) != n:
        return False
    else:
        return isPowerOfTwo(n/2)

print(isPowerOfTwo(18))