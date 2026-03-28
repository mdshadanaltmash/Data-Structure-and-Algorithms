def spiral(matrix):
    op = []
    m, n = len(matrix), len(matrix[0])
    x1, y1 = 0, 0
    x2, y2 = n, m
    while x1 < x2 and y1 < y2:
        for j in range(x1, x2):
            op.append(matrix[y1][j])
        y1 += 1
        for i in range(y1, y2):
            op.append(matrix[i][x2 - 1])
        x2 -= 1
        if not (x1 < x2 and y1 < y2):
            break
        for j in range(x2 - 1, x1 - 1, -1):
            op.append(matrix[y2 - 1][j])
        y2 -= 1
        for i in range(y2 - 1, y1 - 1, -1):
            op.append(matrix[i][x1])
        x1 += 1
    return op


def spiral_again(matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []

    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1

        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1
    return res


a = [[6, 9, 7]]
b = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
c = [[1],
     [2],
     [3]]
print(spiral(c))
print(spiral_again(c))
