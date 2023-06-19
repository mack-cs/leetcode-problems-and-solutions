"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
        dups = set(s[0])
        left, right = 0, 1
        # dups.add(s[0])
        while right < len(s):
            if s[right] not in dups:
                
                
            

s1 = "abcabcbb"
# Output: 3

s2 = "bbbbb"
#Output: 1

s = "pwwkew"
#Output: 3

print(lengthOfLongestSubstring(s1))