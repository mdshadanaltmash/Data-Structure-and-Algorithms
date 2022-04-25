def mult_by_recursion(a, b):
    if b==0 or a==0:
        return 0
    elif b==1:
        return b
    else:
        return mult_by_recursion(a-1, b) + b


def mult_by_karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        z0 = mult_by_karatsuba(b,d)
        z1 = mult_by_karatsuba((a+b),(c+d))
        z2 = mult_by_karatsuba(a,c)

        return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)

a=3141592653589793238462643383279502884197169399375105820974944592
b= 2718281828459045235360287471352662497757247093699959574966967627
print(mult_by_karatsuba(a,b))