"""
Largest Number

Given a list of non-negative integers nums, 
arrange them such that they form the largest number and return it.

Since the result may be very large, 
so you need to return a string instead of an integer.
Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
### Solution 1
from functools import cmp_to_key
def largestNumber(nums):
    for i, n in enumerate(nums):
        nums[i] = str(n)
    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1
    nums =  sorted(nums, key=cmp_to_key(compare))
    return int(int("".join(nums)))  

### Solution 2
from typing import List
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
        