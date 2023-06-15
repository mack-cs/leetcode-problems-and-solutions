from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list) # mapping charCount to list of Anagrams

    for s in strs:
        count = [0] * 26 # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1 #to know position of each letter we subtract its ask value minus ask of "a"
        print(count)
        res[tuple(count)].append(s)
    return res.values()



strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs))