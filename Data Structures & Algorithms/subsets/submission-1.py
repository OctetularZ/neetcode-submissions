class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(idx, path):
            result.append(path[:])

            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return result