"""
Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105
"""
## Bruite Force
def replaceElements(arr):
    if len(arr) == 1:
        return [-1]

    for i  in range(len(arr)):
        max_v = -1
        for j in range(i + 1, len(arr)):
            max_v = max(max_v, arr[j])
        arr[i] = max_v
    return arr
arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# print(replaceElements(arr))
def replaceElements(arr):
    
    for i  in range(len(arr)):
        max_v = -1
        if len(arr[i+1:]) > 0:
            arr_max = max(arr[i+1:])
        else:
            arr_max = -1
        max_v = max(max_v, arr_max)
        arr[i] = max_v
    return arr
arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
print(replaceElements(arr))

## Optimum Solution
def replaceElements(arr):
    # initial max = -1
    # reverse iteration
    # new max = max(oldmax, arr[i])

    rightMax = -1
    for i in range(len(arr)-1, -1, -1):
        newMax = max(arr[i], rightMax)
        arr[i] = rightMax
        rightMax = newMax
    return arr