from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for [key, value] in count.items():
            print(key, value)
            if count[key] > len(nums)/2:
                return key