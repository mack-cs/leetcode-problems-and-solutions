"""
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list) 

    for str in strs:
        counter = [0] * 26
        for c in str:
            counter[ord(c) - ord('a')] += 1
        res[tuple(counter)].append(str)
    return list(res.values())[::-1]
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))