class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        start = 0

        for end in range(len(nums)):
            if len(window) > k:
                window.remove(nums[start])
                start += 1
            if nums[end] in window:
                return True
            else:
                window.add(nums[end])
                
        return False
            
            
