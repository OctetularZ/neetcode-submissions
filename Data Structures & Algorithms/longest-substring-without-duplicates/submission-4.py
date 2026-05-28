class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = set()
        max_length = 0
        start = 0

        for end in range(len(s)):
            while s[end] in state:
                state.remove(s[start])
                start += 1
                
            state.add(s[end])
            max_length = max(max_length, end - start + 1)
        
        return max_length


"abcabcbb"
start = 0
end = 2