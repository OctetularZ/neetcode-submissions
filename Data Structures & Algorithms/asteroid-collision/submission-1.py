class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                if abs(i) > abs(stack[-1]):
                    stack.pop()
                elif abs(i) < abs(stack[-1]):
                    i = 0
                elif abs(i) == abs(stack[-1]):
                    i = 0
                    stack.pop()

            if i:
                stack.append(i)
        
        return stack
        



# Loop through asteroids, and add to stack
# If top of stack is going opposite direction to current asteroid:
# Find the winning asteroid, push winning asteroid onto stack