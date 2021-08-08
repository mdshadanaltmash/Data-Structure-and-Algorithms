def makeAnagram(a, b):
    # Write your code here
    count=0
    for i in a:
        if a.count(i)!=b.count(i):
            count=count+(abs(a.count(i)-b.count(i)))
    for i in b:
        if b.count(i)!=a.count(i):
            count=count+(abs(b.count(i)-a.count(i) ))    
    return count

a = 'crxzwscanmligyxyvym'
b='jxwtrhvujlmrpdoqbisbwhmgpmeoke'

res = makeAnagram(a, b)
print(res)