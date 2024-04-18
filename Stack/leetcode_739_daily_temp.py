def dailyTemperatures(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while stack != [] and temp > stack[-1][1]:
            top_index, top_temp = stack.pop()
            res[top_index] = i - top_index
        stack.append((i, temp))
    return res


temps = [73, 74, 75, 71, 69, 72, 76, 73]
print('Result is ', dailyTemperatures(temps))
