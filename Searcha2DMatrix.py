"""
Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
def searchMatrix(matrix, target):
    for i in matrix:
        if target > i[-1]:
            continue
        elif target <= i[-1]:
            print(f"i[-1]{i[-1]}<==> target{target}")
            left, right = 0, len(i) - 1
            while left <= right:
                mid = (left + right) // 2
                if i[mid] == target:
                    return True
                elif target > i[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            return False
    return False
## Solution 2
def searchMatrix(matrix, target):
    rows = len(matrix)
    if rows == 0:
        return False
    columns = len(matrix[0])
    left, right = 0, rows * columns - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = matrix[mid // columns][mid % columns]
        if mid_element == target:
            return True
        elif target > mid_element:
            left = mid + 1
        else:
            right = mid - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 20
searchMatrix(matrix, target)
print(searchMatrix(matrix, target))     