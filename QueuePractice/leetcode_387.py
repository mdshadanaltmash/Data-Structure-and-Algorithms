'''Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

'''
def firstUniqChar(s) -> int:
    char={}
    for i in s:
        if i in char.keys():
            char[i]=-2
        else:
            char[i]=s.index(i)
            
    for keys,values in char.items():
        if values !=-2:
            return values
    else:
        return -1

string="mdshadanaltmash"
print(firstUniqChar(string))