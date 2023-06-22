"""
Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
s1 = "adc"
s2 = "dcda"
def checkInclusion(s1: str, s2: str) -> bool:
    counter_s1 = [0] * 26
    counter_s2 = [0] * 26

    for ch in s1:
        counter_s1[ord(ch) - ord('a')] += 1

    l = 0
    for r in range(len(s2)):
        counter_s2[ord(s2[r]) - ord('a')] += 1

        if r - l >= len(s1):
            counter_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        if counter_s1 == counter_s2:
            return True

    return False

def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for char in s1:
            s1_counter[ord(char) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            s2_counter[ord(s2[r]) - ord('a')] += 1

            if r - l >= len(s1):
                s2_counter[ord(s2[r]) - ord('a')] -= 1
                l += 1
            if s1_counter == s2_counter:
                return True 

        return False


print(checkInclusion(s1, s2))
"""
The code initializes two lists, counter_s1 and counter_s2, to keep track of the counts of each character in s1 and the 
sliding window of characters in s2, respectively. 
The lists have a size of 26 to account for lowercase English alphabet characters.

The code then iterates over s2 using two pointers, l and r, representing the left and right ends of the sliding window. 
The code increments the count of s2[r] in counter_s2 and checks if the window has reached the size of s1. If it has, 
it decrements the count of s2[l] and moves the left pointer l to the right.

Finally, the code compares counter_s1 and counter_s2 at each step and returns True if they are equal, indicating that s1 
is a permutation of a substring in s2. If no match is found, it returns False.

I assumes that both s1 and s2 consist only of lowercase English alphabet characters. 
If the input strings can contain other characters or be of different character sets, modifications to the code might be 
necessary.
"""
