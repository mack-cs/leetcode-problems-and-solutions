def merge(nums1, nums2):
    i = 0
    j = 0
    merged = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
        
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    
    return merged

nums1 = []
nums2 = [1,2,3,4,5]



from statistics import median
res = median(merge(nums1, nums2))


def find_median(list):
    mid = len(list) // 2

    if mid % 2 == 1:
        median = list[mid]
    else:
        median = (list[mid - 1] + list[mid]) / 2
    return median 

print(find_median(merge(nums1, nums2)))
print(len(nums1))

### Solution 2
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        mid = total_length // 2

        i = 0
        j = 0
        prev = None
        current = None

        while i + j <= mid:
            prev = current
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1

        if total_length % 2 == 0:
            return (prev + current) / 2
        else:
            return current

