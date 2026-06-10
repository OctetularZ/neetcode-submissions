class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(path, index):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[index])
            res.append(path[:])

            for i in range(index + 1, len(nums)):
                backtrack(path, i)
            
            path.pop()
        
        for i in range(len(nums)):
            backtrack([], i)
        return res


# Immediate for loop Backtracking 
# I.e. [1, 2, 3] For loop through 1, 2, 3 and perform a backtrack on each index
# At each step, add to result array
# Base case - if idx/len of path is == to len of input array
# Repeat backtrack for each number in for loop but only include every number expect for itself in search space - so index is needed I.e. if for loop currently has index 0, pass [1:].
# Don’t include that index 0, this avoids duplicates as question stated All numbers unique so don’t have to check for multiple possibilities of same number.