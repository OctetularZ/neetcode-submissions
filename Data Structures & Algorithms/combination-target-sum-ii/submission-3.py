class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(path, total, index):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or index == len(candidates):
                return
            
            path.append(candidates[index])
            backtrack(path, total + candidates[index], index + 1)
            path.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(path, total, index + 1)
        

        backtrack([], 0, 0)
        return res
        

# Backtracking
# Parameters -> (path, total, index)
# 
