"""
Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 
"""
## Solution 1
def isSubsequence(s, t):
    slen = len(s) - 1
    for l in range(len(t) -1, -1, -1):
        if t[l] == s[slen]:
            slen -= 1
    return True if slen < 0 else False

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))

## Solution 2
def isSubsequence(s, t):
    i,j = 0,0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False
        
        