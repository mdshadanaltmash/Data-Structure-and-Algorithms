# User function Template for python3

class Solution:
    def findSubString(self, str):
        # code here
        req_len = len(set(str))
        n = len(str)
        min_len = n
        l = r = 0
        seen = {}

        while r < n:
            seen[str[r]] = seen.get(str[r], 0) + 1


            while len(seen) == req_len:
                # print(seen, end='-->')
                min_len = min(min_len, r - l + 1)
                seen[str[l]] -= 1
                if seen[str[l]] == 0:
                    del seen[str[l]]
                l += 1
            r += 1
        return min_len

obj = Solution()
s = "aabcbcdbca"
print(obj.findSubString(s))