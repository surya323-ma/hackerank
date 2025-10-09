Given a sorted array of integers that may contain duplicates, return the index of the first occurrence of a target value or -1 if not found.
def findFirstOccurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1  # keep searching to the left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
