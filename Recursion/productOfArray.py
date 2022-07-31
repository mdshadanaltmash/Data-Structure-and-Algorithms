def productOfArray(arr):
    if arr==[]:
        return 1
    else:
        return arr[0]*productOfArray(arr[1:])


print(productOfArray([1,2,3,4]))