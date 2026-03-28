def remove_substring(s: str, k: int) -> str:
    stack = []
    for ch in s:
        stack.append(ch)
        # Check if the last 2*k characters form a k-balanced substring
        if len(stack) >= 2 * k and ''.join(stack[-2 * k:]) == '(' * k + ')' * k:
            # print(''.join(stack))
            # print(''.join(stack[-2 * k:]))
            for _ in range(2 * k):
                # print(ch, ''.join(stack))
                stack.pop()  # remove the k-balanced substring

    return ''.join(stack)


s = "(())"
k = 1
print(remove_substring(s, k))
