import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        res = 0

        for i in range(k):
            if i != k - 1:
                heapq.heappop(nums)
            else:
                res = -heapq.heappop(nums)
        
        return res
