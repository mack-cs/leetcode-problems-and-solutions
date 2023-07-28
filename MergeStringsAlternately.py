"""
Merge Strings Alternately
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
#### Solution 1
def mergeAlternately(word1,word2):
    j, k = 0, 0
    count = 0
    res = ""
    while j < len(word1) and k < len(word2):
        if count % 2:
            res += word2[k]
            k += 1
        else:
            res += word1[j]
            j += 1
        count += 1
    if j < len(word1):
        res += word1[j:]
    if k < len(word2):
        res += word2[k:]
    return res
### Solution 1 Improved
def mergeAlternately(self, word1: str, word2: str) -> str:
    j, k = 0, 0
    count = 0
    res = []
    while j < len(word1) and k < len(word2):
        if count % 2:
            res.append(word2[k])
            k += 1
        else:
            res.append(word1[j])
            j += 1
        count += 1
    if j < len(word1):
        res.append(word1[j:])
    if k < len(word2):
        res.append(word2[k:])
    return "".join(res)

#### Solution 1 improved further 
def mergeAlternately(word1, word2):
    j, k = 0, 0
    res = []
    while j < len(word1) and k < len(word2):
        res.append(word1[j])
        res.append(word2[k])
        k += 1
        j += 1
    if j < len(word1):
        res.append(word1[j:])
    if k < len(word2):
        res.append(word2[k:])
    return "".join(res)

word1 = "abc"
word2 = "pqr"
# Output: "apbqcd"
print(mergeAlternately(word1,word2))