## LeetCode 844. Backspace String Compare
'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

'''


def backspaceCompare( s: str, t: str) -> bool:
        st=[]
        ts=[]
        for i in range(len(s)):
            if s[len(s)-1-i]=='#':
                if st==[]:
                    continue
                else:
                    st.pop()
            else:
                st.append(s[len(s)-1-i])
                
        for i in range(len(t)):
            if t[len(t)-1-i]=='#':
                if ts==[]:
                    continue
                else:
                    ts.pop()
            else:
                ts.append(t[len(t)-1-i])
        return st==ts

s="a#c"
t="b"
print(backspaceCompare(s,t))