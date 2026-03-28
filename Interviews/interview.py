s = 'aaliya'
s = s[::-1]
print(s[::-1])

l, r = 0, len(s)-1
a = ''
b = ''
while r>=l:
    a = a + s[r]
    if l!=r:
        b = s[l] + b
    l+=1
    r-=1
print(a+b)

