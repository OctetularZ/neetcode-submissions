from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        frequencies_lst = []

        for num in frequencies:
            freq = frequencies[num]
            frequencies_lst.append((freq, num))
        
        frequencies_lst.sort()
        result = []

        for freq, num in frequencies_lst:
            result.append(num)
        
        result.reverse()
        return result[:k]