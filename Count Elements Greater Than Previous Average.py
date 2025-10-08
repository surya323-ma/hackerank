Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    count = 0
    total = 0

    for i in range(1, len(responseTimes)):
        total += responseTimes[i - 1]
        avg = total / i
        if responseTimes[i] > avg:
            count += 1

    return count
