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

#### Solution: 1
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

#### Solution: 2
def subarraySum(nums, k):
    """
    To solve this problem, we can use the concept of cumulative sums and hash maps to efficiently find the total 
    number of subarrays whose sum equals to k. The idea is to keep track of the cumulative sum at each index while 
    traversing the array and then use a hash map to count the occurrences of specific cumulative sums.

    Let's break down the steps of the solution:

    Step 1: Initialize variables
    - Initialize a variable `count` to keep track of the total number of subarrays whose sum equals to k.
    - Initialize a variable `cumulativeSum` to keep track of the cumulative sum while traversing the array.
    - Initialize a hash map `sumCount`, where the key represents the cumulative sum, and the value represents the 
    number of times that sum has occurred so far.

    Step 2: Traverse the array
    - Iterate through the array `nums`, starting from the first element.
    - At each index, update the `cumulativeSum` by adding the current element's value.
    - Check if `cumulativeSum - k` exists in the `sumCount` hash map. If it does, it means there are some subarrays that sum up to k.
    - Increment the `count` by the number of occurrences of `cumulativeSum - k` in the `sumCount` hash map.
    - Update the `sumCount` hash map by incrementing the count of `cumulativeSum` by 1.

    Step 3: Return the result
    - After traversing the entire array, return the `count` variable, which represents the total number of subarrays whose sum equals to k.


    # Test cases
    nums1 = [1, 1, 1]
    k1 = 2
    print(subarraySum(nums1, k1))  # Output: 2

    nums2 = [1, 2, 3]
    k2 = 3
    print(subarraySum(nums2, k2))  # Output: 2
    ```

    In the example provided, the first test case `[1, 1, 1]` with `k = 2` has two subarrays `[1, 1]` and `[1, 1]`,
      both of which sum up to 2, so the output is 2. 
      The second test case `[1, 2, 3]` with `k = 3` has two subarrays `[1, 2]` and `[3]`, which also sum up to 3,
        resulting in an output of 2.
    """
    count = 0
    cumulativeSum = 0
    sumCount = {0: 1}  # Initialize the hash map with 0 to handle subarrays starting from the beginning.

    for num in nums:
        cumulativeSum += num

        # Check if there is any subarray whose sum equals k.
        if cumulativeSum - k in sumCount:
            count += sumCount[cumulativeSum - k]

        # Increment the count of current cumulative sum in the hash map.
        sumCount[cumulativeSum] = sumCount.get(cumulativeSum, 0) + 1

    return count


### Solution: 3
def subarraySum(nums, k):
    res = 0
    curSum = 0
    prefixSum = {0: 1}

    for n in nums:
        curSum += n
        diff = curSum - k
        res += prefixSum.get(diff, 0)
        prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
    return res

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