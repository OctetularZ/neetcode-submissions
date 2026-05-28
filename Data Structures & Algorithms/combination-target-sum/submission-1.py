class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, path, total):
            if total == target:
                result.append(path[:])
            
            if total > target:
                return
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i, path, total + nums[i])
                path.pop()
        
        dfs(0, [], 0)
        return result