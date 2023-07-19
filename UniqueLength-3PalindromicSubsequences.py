"""
Unique Length-3 Palindromic Subsequences
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
"""

### Bruite Force
def countPalindromicSubsequence(s):
    palindroms = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if s[i]+s[j]+s[k] == s[k]+s[j]+s[i]:
                    palindroms.add((s[i], s[j], s[k]))
    return len(palindroms)

s = "bbcbaba"
# Output: 4
print(countPalindromicSubsequence(s))

### Improved Bruite Force 
def countPalindromicSubsequence(s):
    n = len(s)
    palindroms = set()

    # Helper function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]

    # Iterate through all possible characters and find palindromic subsequences
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                subseq = s[i] + s[j] + s[k]
                if is_palindrome(subseq):
                    palindroms.add(subseq)

    return len(palindroms)

s ="""nhzosdwmwomlebymvkbqbdohzdtpufnllwzhqptyffreebalphgsslryuqryloqxvbehtohdrsynm
cbligczvoyzrhbtmqxepqmcjirwishyvoliizknzrokejtqtfoylsdzpgeooczxldvmsnhvzgojxnwwhukynvh
hpzmdoiooliesogubtsvkrvzmanpwwlnlskremzisqwwwjistwabqxztlcqwlsxbuhjdnouecwqgxdlggauxre
lipqlgvfkmgoozhzrhortbpmxhupjqqrsrvqxqilptchtedoznxvgvmuticzdzwszzujuanlrrpvycgawoxfbv
xhkdyhmcxdlrtyktekcmkyajlywcrozjkedwlrqpaugdobtffwidxawddgeraaugiebtntmuncnybuwnlzbmkr
mxbcpbhqoiznlpcswqtsflfilkclrjdxbvcctvopoidjrtwszpjpfrfcvjtouvzvpqayvgesiiawokdqatfkij
suocbeqrhrmlhtclhrmrbkpahfdgiatejsnvubwbaxwooskcaiuqvxcvgpnkiiiencnxjsvvgdfptreumttlyo
qqwqdblhhbnilbvbwwpnmouxlvqimdbcxisnegllnejhkipuqbcrhsrxwipdjzskpyijuvrvtrnqljjefymfdc
vcuvwaitdjevuvelkrglhtlnivmvjyzmhjnzvudgqwocvwhthxdlyfljabngzjayvqudhvsdslacgvosnchhbk
ulcxpangdlpgkrczbnnzokmqzgauitqutiboveumsqvbulhbfbynzogtejuwi"""


## Improved 
import collections
def countPalindromicSubsequence(s):
    res = set()
    left = set()
    right = collections.Counter(s)

    for i in range(len(s)): # Everytime we get to a char it becomes our middle char,
        right[s[i]] -= 1 # meaning its no longer part of the [right] portion
        if right[s[i]] == 0:
            right.pop(s[i])

        for j in range(26):
            c = chr(ord('a') + j)
            if c in left and c in right:
                res.add((s[i], c))
        left.add(s[i])
    return len(res)

    
    # return len(palindroms)

print(countPalindromicSubsequence(s))

