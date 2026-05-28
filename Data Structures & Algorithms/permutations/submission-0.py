class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def dfs(idx, path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            if len(path) > len(nums):
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
                used[i] = False

        dfs(0, [])
        return result