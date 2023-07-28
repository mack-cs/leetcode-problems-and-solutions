"""
Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
def validPalindrome(s):
    l, r = 0 , len(s)-1

    while l < r:
        if s[l] != s[r]:
            skipL, skipR = s[l + 1:r+1], s[l:r]
            return (skipL == skipL[::-1] or skipR == skipR[::-1])
        l += 1
        r -= 1
    return True
s = "abcka"
# Output: true
print(validPalindrome(s))