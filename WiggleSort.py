"""
ChatGPT
"Wiggle Sort" is a problem on LeetCode that involves reordering an array of integers in a specific way. The problem statement is as follows:

Given an unsorted array of integers, rearrange the array in a "wiggle" order. A "wiggle" order is when the elements of the array are in the following form:

nums[0] <= nums[1] >= nums[2] <= nums[3] >= nums[4] <= ...

In other words, the elements are alternately in ascending and descending order.

Here's an example:

Input: [3, 5, 2, 1, 6, 4]
Output: [3, 5, 1, 6, 2, 4]

To solve this problem, you can use a simple sorting approach or a more efficient in-place swapping approach. Here, I'll explain the in-place approach, which has a time complexity of O(n) and space complexity of O(1).

In-Place Approach:

Iterate through the array starting from
To solve this problem, you can use a simple sorting approach or a more efficient in-place swapping approach. Here, I'll explain the in-place approach, which has a time complexity of O(n) and space complexity of O(1).
"""
def wiggleSort(nums):
    for i in range(1, len(nums)):
        if ((i % 2 == 1 and nums[i] < nums[i - 1]) or
        (i % 2 == 0 and nums[i] > nums[i - 1])):
            nums[i], nums[i - 1] = nums[i - 1],nums[i]
    return nums

nums =  [3, 5, 2, 1, 6, 4]
# Output: [3, 5, 1, 6, 2, 4]
print(wiggleSort(nums))