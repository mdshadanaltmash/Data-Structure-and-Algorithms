# find missing number between range 1 to n


def missing_num(arr,n):
    range_sum = (n*(n+1))/2
    list_sum= sum(arr)
    return (range_sum - list_sum)
    
n=100
array = [i for i in range(n+1)]
array.remove(78)
print(missing_num(array,100))