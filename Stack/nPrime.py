prime=[2]
q=int(input())
j=2
while len(prime)!=q:
    j+=1
    for i in range (2,(j//2)+1):
        if j%i==0:
            break
    else:
        prime.append(j)
print(prime)