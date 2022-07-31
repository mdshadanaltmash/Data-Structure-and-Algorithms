def decToBin(n):
    if n<2:
        return n
    else:
        return 10*decToBin(n//2)+n%2
print(decToBin(3))