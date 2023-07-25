"""
Optimal Partition of String
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.
Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.
"""
### Version 1
def partitionString(s):
    res = []
    left, right = 0, 1
    while right < len(s):
        if s[right] not in s[left:right]:
            right += 1
        else:
            res.append(s[left:right])
            left = right
            right += 1
    res.append(s[left])
    return len(res)
### Version 2
def partitionString(s):
    res = 0
    left, right = 0, 1
    while right < len(s):
        if s[right] not in s[left:right]:
            right += 1
        else:
            res += 1
            left = right
            right += 1
    res += 1
    return res

### Version 3
def partitionString(s):
    res = 0
    curSet = set()

    for c in s:
        if c in curSet:
            res += 1
            curSet = set()
        curSet.add(c)
    res += 1
    return res
s = "abacaba"
# Output: 4
print(partitionString(s))

s = "ssssss"
# Output: 6
print(partitionString(s))