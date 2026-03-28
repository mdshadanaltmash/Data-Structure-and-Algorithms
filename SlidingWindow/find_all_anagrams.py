"""
Given two strings s and p, return an array of all the start indices of p's
anagrams
 in s. You may return the answer in any order.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
LINK: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""


def get_anagrams_index(s, p):
    map_s = dict()
    map_p = dict()
    p_len = len(p)

    for c in p:
        map_p[c] = map_p.get(c, 0) + 1

    for i in range(p_len):
        map_s[s[i]] = map_s.get(s[i], 0) + 1
    res = []
    if map_p == map_s:
        res.append(0)
    for i in range(p_len, len(s)):
        prev = s[i-p_len]
        if map_s[prev] == 1:
            map_s.pop(prev)
        else:
            map_s[prev] = map_s[prev] - 1
        map_s[s[i]] = map_s.get(s[i], 0) + 1

        if map_s == map_p:
            res.append(i-p_len+1)
    return res


s = "ababc"
p = "abc"

print(get_anagrams_index(s, p))
