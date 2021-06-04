number=[3,4,7,6,5]
q=1
prime=[2]
j=2
while len(prime)!=q:
    j+=1
    for i in range (2,(j//2)+1):
        if j%i==0:
            break
    else:
        prime.append(j)
itr=0
b=[]
b0=[]
a=[]
while itr<q and number!=[]:
    while number!=[]:
        n=number.pop()
        if n%prime[itr]==0:
            b0.append(n)
        else:
            a.append(n)
    number=a
    a=[]
    while b0!=[]:
        b.append(b0.pop())
    itr+=1
while number!=[]:
    b.append(number.pop())
print(b)