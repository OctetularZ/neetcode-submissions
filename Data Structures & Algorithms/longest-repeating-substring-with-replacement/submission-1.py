class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        start = 0
        max_freq = 0
        state = {}

        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1
            max_freq = max(max_freq, state[s[end]])

            while end - start + 1 - max_freq > k:
                state[s[start]] -= 1
                start += 1
                if state[s[start]] == 0:
                    del state[s[start]]
            
            
            max_length = max(max_length, end - start + 1)
    
        return max_length
        


# Dict - Store each element and it's frequency
# When length of dictionary is more than k + 1, keep removing start of window until length of dict becomes less than s[start] is gone
# Keep adding to dict until len more than k + 1
