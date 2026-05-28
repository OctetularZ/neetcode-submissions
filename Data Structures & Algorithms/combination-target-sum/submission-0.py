class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(idx, subset, total):
            if total == target:
                result.append(subset[:])
                return
            
            if idx >= len(nums) or total > target:
                return
            
            subset.append(nums[idx])
            backtrack(idx, subset, total + nums[idx])
            subset.pop()
            backtrack(idx + 1, subset, total)
        
        backtrack(0, [], 0)
        return result
