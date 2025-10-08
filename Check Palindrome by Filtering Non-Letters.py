Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

def isAlphabeticPalindrome(code):
    # Write your code here
    filtered = [c.lower() for c in code if c.isalpha()]
    return filtered == filtered[::-1]
