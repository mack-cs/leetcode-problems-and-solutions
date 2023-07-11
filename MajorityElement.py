"""
Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
def majorityElement(nums):
    counter = {}
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
    for k, v in counter.items():
        if v > (len(nums) / 2):
            return k
    return 

nums = [2,2,1,1,1,2,2]
# Output: 2
print(majorityElement(nums))

## Solution 2
def majorityElement(nums):
    counter = {}
    res, maxCount = 0, 0
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
        res = n if counter[n] > maxCount else res
        maxCount = max(maxCount, counter[n])
    return res

nums = [2,2,1,1,1,2,2]
# Output: 2
print(majorityElement(nums))

## Bo
