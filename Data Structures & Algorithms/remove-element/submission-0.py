class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0

        while val in nums:
            nums.remove(val)
            counter += 1
        
        return len(nums)