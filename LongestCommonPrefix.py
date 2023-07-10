"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
def longestCommonPrefix(strs):
    word = strs[0]
    found = ""
    for i in range(len(word)):
        count = 1
        for str in strs[1:]:
            if i <= len(str) - 1 and word[i] == str[i]:
                count += 1
            else:
                print(f"False index [{i}-{word[i]}]{len(str) -1}")
                return found
        if count == len(strs):
            print(f"{count}-{len(strs)}")
            found += word[i]
    return found
strs = ["ab", "a"]

### Improved Code
def longestCommonPrefix(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]
print(longestCommonPrefix(strs))