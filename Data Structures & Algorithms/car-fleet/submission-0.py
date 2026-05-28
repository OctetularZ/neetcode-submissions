class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(p, r) for p, r in zip(position, speed)]
        times.sort(reverse=True)

        stack = []
        for p, r in times:
            stack.append((target - p)/ r)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)