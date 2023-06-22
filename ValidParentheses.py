"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
s1 = "()"
#Output: true
s2 = "()[]{}"
#Output: true
s3 = "(]"
#Output: false

def isValid(s):
    stack = []
    closeToOpen = {"}":"{","]":"[",")":"("}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:#If its closing bracket make sure the stack is not empty and last element is the opening of current
                stack.pop(c) #If the closing match the opening we remove it
            else:
                #If they dont match and stack is empty
                return False
        else:
            # If we get an open parenthesis we append to the stack
            stack.append(c)
    ## If stack is empty we return true
    return True if not stack else False
isValid(s2)
        
