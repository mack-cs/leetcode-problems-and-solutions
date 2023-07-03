def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midoint of the list and divide into sublists
    Conquer: Recursively sort the sublists creted in previous ste
    Combine: Merge time sorted sublits created in previous step

    Takes O(n log n) time
    """

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublits
    Returns two sublists - left and right

    Takes overall O(log n) time
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

def verify_sorted(list):
    n = len(list)
    if n <= 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])

if __name__ == "__main__":
    alist = [87,4,1,77,34,22,74,9,1,0,67,44,1,90]
    print(f"Is in put list sorted? {verify_sorted(alist)}")
    alist_sorted = merge_sort(alist)
    print(f"Is in output list sorted? {verify_sorted(alist_sorted)}")
