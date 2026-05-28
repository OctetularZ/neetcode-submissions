class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if token == '+':
                    stack.append(num1 + num2)
                if token == '-':
                    stack.append(num1 - num2)
                if token == '*':
                    stack.append(num1 * num2)
                if token == '/':
                    stack.append(num1 / num2)
            else:
                stack.append(token)
        
        return int(stack[-1])


# Stack
# Create a set to check if we encouter any operations
# Add onto stack if not an operator
# When we encounter an operator, pop all elements from stack and perform operation, add result back onto stack
# Return top of stack
