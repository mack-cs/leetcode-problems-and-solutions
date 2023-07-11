"""
Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 
0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
### Solution 1
def canPlaceFlowers(flowerbed, n):
    res = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(2,len(flowerbed)):
        p1, p2, p3 = flowerbed[i-2],flowerbed[i-1], flowerbed[i]
        if p1 == 0 and p2 == 0 and p3 == 0:
            res += 1
            flowerbed[i-1] = 1 
    return flowerbed,True if res >= n else False


flowerbed = [1,0,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))

### Solution 2
def canPlaceFlowers(flowerbed, n):
    f = [0] + flowerbed + [0]
    for i in range(1, len(f) - 1):
        if f[i - 1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n - 1
    return n == 0
flowerbed1 = [1,0,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed1, n))


