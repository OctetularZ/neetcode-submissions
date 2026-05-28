class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        arr = []

        def backtrack(idx):
            if idx >= len(nums):
                result.append(arr[:])
                return
            
            arr.append(nums[idx])
            backtrack(idx + 1)
            arr.pop()
            backtrack(idx + 1)

            return
        
        backtrack(0)
        
        return result
            
