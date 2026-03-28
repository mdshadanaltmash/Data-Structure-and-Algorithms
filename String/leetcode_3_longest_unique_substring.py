class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = left = right = 0
        seen = dict()

        while len(s) > right >= left:
            if s[right] not in seen:
                seen[s[right]] = right
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                while left != seen[s[right]] and left < right:
                    seen.pop(s[left])
                    left += 1
                seen.pop(s[left])
                left += 1
        return max_len


obj = Solution()
print(obj.lengthOfLongestSubstring('abcabc'))
