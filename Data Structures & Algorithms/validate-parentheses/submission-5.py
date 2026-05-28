class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for bracket in s:
            if stack and bracket in bracket_map:
                if bracket_map[bracket] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        
        return len(stack) == 0
        

# Stack
# Each time an open bracket is found, add to stack
# Create dict for O(1) lookups {')': '('}
# If top of stack != its closing bracket, return False
# Otherwise, pop from stack
