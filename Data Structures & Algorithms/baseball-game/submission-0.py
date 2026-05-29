class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1)
                stack.append(num2)
                stack.append(num1 + num2)
            elif op == "D":
                top = stack[-1]
                stack.append(top * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)