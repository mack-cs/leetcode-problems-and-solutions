"""
Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
Accepted
929.5K
Submissions
2.2M

"""

def isIsomorphic(s, t):
    s_set, t_set = {}, {}

    for ch1, ch2 in zip(s, t):
        if ((ch1 in s_set and s_set[ch1] != ch2)
            or ch2 in t_set and t_set[ch2] != ch1):
            return False
        s_set[ch1] = ch2
        t_set[ch2] = ch1
    return True
s = "egg"
t = "add"
# Output: true
print(isIsomorphic(s, t))

s = "foo"
t = "bar"
# Output: false
print(isIsomorphic(s, t))

s = "paper"
t = "title"
# Output: true
print(isIsomorphic(s, t))