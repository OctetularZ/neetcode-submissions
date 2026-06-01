class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        return slow
        


# Floyds Algorithm
# Find cycle, intially find where two pointers, slow and fast meet.
# Then create a second slow pointer and find where it meets with intial slow pointer
# Then you've found the duplicate.