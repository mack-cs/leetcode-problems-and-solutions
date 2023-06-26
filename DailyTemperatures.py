"""
 Daily Temperatures
Medium
10.9K
243
Companies
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
## Brute Force
def dailyTemperatures(temperatures):
    output = [0] * len(temperatures)
    for i in range(len(temperatures)):
        j = i + 1
        while  j < len(temperatures):
            if temperatures[i] < temperatures[j]:
                output[i] = (j - i)
                break
            j += 1
    return output

## O(n)
def dailyTemperatures(temperatures):
    output = [0] * len(temperatures)
    stack = [] # index and temp
    for i,t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            output[stackInd] = (i - stackInd)
        stack.append([t, i])
    return output

temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
print(dailyTemperatures(temperatures))

temperatures = [30,40,50,60]
# Output: [1,1,1,0]
print(dailyTemperatures(temperatures))

temperatures = [30,60,90]
# Output: [1,1,0]
print(dailyTemperatures(temperatures))