Given two strings s1 and s2, return 1 if s2 is a rotation of s1 but not identical to s1, otherwise return 0.
def isNonTrivialRotation(s1, s2):
    # Write your code here
    if len(s1) == len(s2) and s1 != s2:
        # Check if s2 is a rotation of s1
        return s2 in (s1 + s1)
    return False
