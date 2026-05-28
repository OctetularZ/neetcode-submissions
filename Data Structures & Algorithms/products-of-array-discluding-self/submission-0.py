class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sums = [0] * len(nums)

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            
            prefix_sums[i] = prod
        
        return prefix_sums