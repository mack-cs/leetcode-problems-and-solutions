"""
Find the Difference of Two Arrays
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:
"""
### Solution 1
def findDifference(nums1, nums2):
    size = max(len(nums1), len(nums2))
    nums1res, nums2res = [], []
    for i in range(size):
        if i < len(nums1) and nums1[i] not in nums2:
            if nums1[i] not in nums1res:
                nums1res.append(nums1[i])
        if i < len(nums2) and nums2[i] not in nums1:
            if nums2[i] not in nums2res:
                nums2res.append(nums2[i])
    return [nums1res, nums2res]

#Solution 2
def findDifference(nums1, nums2):
    nums1Set, nums2Set = set(nums1), set(nums2)
    res1, res2 = set(), set()
    for n in nums1Set:
        if n not in nums2Set:
            res1.add(n)
    for n in nums2Set:
        if n not in nums1Set:
            res2.add(n)
    return [list(res1), list(res2)]

#Solution 3
def findDifference(nums1, nums2):
    nums1Set, nums2Set = dict(enumerate(nums1)), dict(enumerate(nums2))
    res1, res2 = set(), set()
    size = max(len(nums1Set), len(nums2Set))
    for i in range(size):
        if i < len(nums1Set) and nums1Set[i] not in nums2Set:
            res1.add(nums1Set[i])
        if i < len(nums2Set) and nums2Set[i] not in nums1Set:
            res2.add(nums2Set[i])
    
    return [list(res1), list(res2)]
nums1 = [1,2,3]
nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
print(findDifference(nums1, nums2))

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
# Output: [[3],[]]
print(findDifference(nums1, nums2))