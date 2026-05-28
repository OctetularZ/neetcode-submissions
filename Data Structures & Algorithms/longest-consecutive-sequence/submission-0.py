class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        max_length = 0

        for num in nums:
            length = 1
            while (num + length) in numsSet:
                length += 1
            
            max_length = max(max_length, length)
        
        return max_length