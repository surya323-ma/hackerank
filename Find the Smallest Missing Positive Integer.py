Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.

def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    for i in range(n):
        while 1 <= orderNumbers[i] <= n and orderNumbers[orderNumbers[i] - 1] != orderNumbers[i]:
            correct_index = orderNumbers[i] - 1
            orderNumbers[i], orderNumbers[correct_index] = orderNumbers[correct_index], orderNumbers[i]
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1
    return n + 1
