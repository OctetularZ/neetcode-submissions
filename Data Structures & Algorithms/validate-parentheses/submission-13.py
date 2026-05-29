class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for bracket in s:
            if bracket not in close_brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                curr = stack[-1]
                if curr != close_brackets[bracket]:
                    return False
                stack.pop()
        
        return not stack