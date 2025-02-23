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


a = [[6, 9, 7]]
b = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
print(spiral(b))
