"""
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

def subarraySum(nums, k):
    count = 0
    sum_dict = {0: 1}
    current_sum = 0

    for num in nums:
        current_sum += num
        if current_sum - k in sum_dict:
            count += sum_dict[current_sum - k]
        if current_sum in sum_dict:
            sum_dict[current_sum] += 1
        else:
            sum_dict[current_sum] = 1

    return count

nums = [1,1,1]
k = 2
# Output: 2
# print(subarraySum(nums, k))            

nums = [1,2,3]
k = 3
# Output: 2
# print(subarraySum(nums, k)) 

nums = [-1,-1,1]
k = 0
print(subarraySum(nums, k))