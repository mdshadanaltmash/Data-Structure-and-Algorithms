"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
 and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:
Input: s = "God Ding"
Output: "doG gniD"
 
Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

def reverseWords(s: str) -> str:
    arr = s.split()
    arr_word = []
    for i in arr:
        st =''
        for j in range(len(i)-1,-1,-1):
            st+=i[j]
            
        arr_word.append(st)
    return ' '.join(arr_word)

a = "Let's take LeetCode contest"
print(reverseWords(a))