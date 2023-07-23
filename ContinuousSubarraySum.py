"""
Continuous Subarray Sum
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
"""
### Bruite Force
def checkSubarraySum(nums, k):
    if sum(nums) % k == 0:
        return True
    else:
        for i in range(len(nums)):
            subSum = nums[i]
            for j in range(i + 1,len(nums)):
                subSum += nums[j]
                if subSum % k == 0:
                    return True
    return False
nums = [23,2,4,6,7]
k = 6
# Output: true
print(checkSubarraySum(nums, k))
nums = [23,2,6,4,7]
k = 6
# Output: true
print(checkSubarraySum(nums, k))
nums = [23,2,6,4,7]
k = 13
# Output: false
print(checkSubarraySum(nums, k))

### Best Solution
def checkSubarraySum(nums, k):
    """
    Loops through array once, adding each element to the total variable.
    Calculates the remender of current total % k and store it in a hashmap
    that stores reminder as key and index as value.

    If the value that of remainder is found in the hashmap and the index from that value
    to current is greater than 1 we have found the sub array that result to true
    """
    remainder = {0:-1} # map remainder -> end index
    total = 0

    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder[r] > 1:
            return True
    return False


