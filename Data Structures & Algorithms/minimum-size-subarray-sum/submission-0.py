class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_length = float('inf')
        window_sum = 0

        for end in range(len(nums)):
            window_sum += nums[end]

            while window_sum >= target:
                min_length = min(min_length, end - start + 1)
                window_sum -= nums[start]
                start += 1
        
        return min_length if min_length != float('inf') else 0





# Sliding window
# Expand window until sum of window greater than or equal to target
# If true, update min_length variable
# Then keep removing start and recalculate min_length each time