"""
Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
## Solution 1
import re
def isPalindrome(s: str) -> bool:
    clean_str = re.sub(r"[\W_]+","",s)
    reversed_str = clean_str.lower()[::-1]
    if clean_str.lower() == reversed_str:
        return True
    else:
        return False
## Solution 2
def isPalindrome2(s: str) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum(): #Use of built in function
            newStr += c.lower()
    return newStr == newStr[::-1] #use of extra memory

## Solution 3 using pointerswithout creating extra memory
## 0n and memory 01
def isPalindrome3( s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or 
     ord('a') <= ord(c) <= ord('z') or
     ord('0') <= ord(c) <= ord('9') 
     )