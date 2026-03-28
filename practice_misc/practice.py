class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        res = 0
        for u in range(1, 4):
            freq = [0, 0, 0]
            left = 0
            distinct = 0

            for right, ch in enumerate(s):
                idx = ord(ch) - 97
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1

                while distinct > u:
                    li = ord(s[left]) - 97
                    freq[li] -= 1
                    if freq[li] == 0:
                        distinct -= 1
                    left += 1

                if distinct == u:
                    base = None
                    ok = True
                    for v in freq:
                        if v > 0:
                            if base is None:
                                base = v
                            elif v != base:
                                ok = False
                                break
                    if ok:
                        res = max(res, right - left + 1)
        return res


obj = Solution()
print(obj.longestBalanced('aabcc'))
