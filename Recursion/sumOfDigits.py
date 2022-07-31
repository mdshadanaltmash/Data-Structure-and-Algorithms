def sumOfDigits(n):
    assert n>=0 and int(n)==n, 'Fibonnacci numbers cannot be negative numbers or non integer.'
    if n <10 :
        return n
    else:
        return n%10 +sumOfDigits(n//10)

print(sumOfDigits(163421))