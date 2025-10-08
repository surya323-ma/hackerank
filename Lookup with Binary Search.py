Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found.\
def binarySearch(nums, target):
    # Write your code here
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
