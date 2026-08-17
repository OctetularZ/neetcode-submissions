class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        intsct = set(nums1).intersection(nums2)
        return list(intsct)