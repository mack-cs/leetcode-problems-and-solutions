"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""
"""
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
def encode(strs):
    # write your code here
    res =''
    for word in strs:
        res += str(len(word)) + "#" + word
    return res

"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(str_):
    # write your code here
    res, i = [], 0
    while i < len(str_):
        j = i
        while str_[j] != "#":
            j += 1
        length = int(str_[i:j])
        print(length)
        res.append(str_[j + 1: j + length + 1])
        i = j + length + 1
    return res
# def decode(str_):
#     res = []
#     i = 0

#     while i < len(str_):
#         j = i
#         while str_[j] != "#":
#             j += 1
#         length = int(str_[i:j])
#         segment = str_[j + 1: j + length + 1]
#         res.append(segment)
#         i = j + length + 1

#     return res


Input = ["we", "say", ":", "yes"]
encoded = encode(Input)
print(encoded)
print(decode(encoded))