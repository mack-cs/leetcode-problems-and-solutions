"""
11. Container With Most Water
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""
height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
## Brute Force
def maxArea(height):
    res = 0
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            min_ = min(height[l], height[r])
            print(f"{res}={r} - {l} * {min_}")
    return res
# print(maxArea(height))
## Optimised
def maxArea(height):
    res = 0
    left, right = 0, len(height) - 1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)
        if height[left] < height[right]:
            left += 1
        else: ## Covers for both when right is small or when left == right
            right -= 1
    return res