class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        res = [0] * len(nums)

        for i in range(len(nums)):
            new_pos = (i + k) % len(nums)
            res[new_pos] = nums[i]
        
        nums[:] = res
        