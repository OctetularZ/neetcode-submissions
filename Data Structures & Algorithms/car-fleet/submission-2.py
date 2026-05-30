class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(p, r) for p, r in zip(position, speed)]
        times.sort(reverse=True)

        stack = []

        for p, r in times:
            calc = (target - p) / r
            stack.append(calc)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)



# Put position and speed into a list of tuples and sort by position
# So the first position in the list is the closest to target
# Loop through list, calculate time target is reached, add to stack
# While len(stack) >= 2 and new calculated time is less than or equal to top of stack:
# Pop from stack, part of the same fleet
# Otherwise, leave it, meaning a new fleet has started.