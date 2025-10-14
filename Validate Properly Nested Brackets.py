Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.

def areBracketsProperlyMatched(code_snippet):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in code_snippet:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return not stack  # True if stack is empty, else False
