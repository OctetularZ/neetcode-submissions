class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(idx, path):
            result.append(path[:])

            if len(path) > len(nums):
                return
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
                
        
        dfs(0, [])
        return result