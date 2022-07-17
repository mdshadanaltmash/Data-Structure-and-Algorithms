def closest_pair(point, n):
    p = [x[0] for x in point]
    p.sort()
    q = [x[1] for x in point]
    q.sort()
    return (closest(p,q, n))

def closest(p,q, n):
    if n < 4:
        pass

    mid = n//2
    midPoint = p[mid]
    pl = p[:mid]
    pr = p[mid+1:]
    



point = [[1,3], [4,3],[5,6],[2,1],[4,3],[3,6]]
print(closest_pair(point, len(point)))