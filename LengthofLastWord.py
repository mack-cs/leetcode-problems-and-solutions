"""
Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
"""
# Solution 1
def lengthOfLastWord(s):
    return len(s.strip().split(" ")[-1])

s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))

# Solution 2
def lengthOfLastWord(s):
    i, length = len(s) - 1, 0

    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length