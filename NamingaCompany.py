"""
Naming a Company
Hard
1.9K
66
Companies
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

 

Example 1:

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.
 

Constraints:

2 <= ideas.length <= 5 * 104
1 <= ideas[i].length <= 10
ideas[i] consists of lowercase English letters.
All the strings in ideas are unique.
"""
from collections import defaultdict
def distinctNames(ideas):
    # map 1st char -> list of word sufixes
    wordMap = defaultdict(set)
    for w in ideas:
        wordMap[w[0]].add(w[1:])

    res = 0
    for char1 in wordMap:
        for char2 in wordMap:
            if char1 == char2:
                continue
            intersect = 0
            for w in wordMap[char1]:
                if w in wordMap[char2]:
                    intersect += 1
            distinct1 = len(wordMap[char1]) - intersect
            distinct2 = len(wordMap[char2]) - intersect
            print(f"{distinct1}-{distinct2}")
            res += distinct1 * distinct2
    return res

#### Simplified Version
def distinctNames(ideas):
    res = 0
    wordMap = {}

    for w in ideas:
        first_char = w[0]
        suffix = w[1:]
        wordMap.setdefault(first_char, set()).add(suffix)

    for char1, suffixes1 in wordMap.items():
        for char2, suffixes2 in wordMap.items():
            if char1 == char2:
                continue
            intersect = len(suffixes1 & suffixes2)
            distinct1 = len(suffixes1) - intersect
            distinct2 = len(suffixes2) - intersect
            res += distinct1 * distinct2

    return res

### Simplified version 2
def distinctNames(ideas):
    wordMap = defaultdict(set)
    res = 0

    for idea in ideas:
        wordMap[idea[0]].add(idea[1:])
    
    for char1, suffixes1 in wordMap.items():
        for char2, suffixes2 in wordMap.items():
            if char1 == char2:
                continue
            intersection = len(suffixes1 & suffixes2) 
            distinct1 = len(wordMap[char1]) - intersection
            distinct2 = len(wordMap[char2]) - intersection
            res += distinct1 * distinct2
    return res

ideas = ["coffee","donuts","time","toffee"]
print(distinctNames(ideas))