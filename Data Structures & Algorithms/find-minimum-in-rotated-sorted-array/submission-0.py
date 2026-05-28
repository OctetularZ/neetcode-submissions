class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + (right - 1)) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]



# Half of array always sorted
# Find middle of array, if left half is less than middle value, search left half, otherwise, search right half
# Eventually, you will end up being in the section of the array which is sorted.
