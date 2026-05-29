class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        start = 0
        res = 0
        max_freq = 0

        for end in range(len(s)):
            window[s[end]] = window.get(s[end], 0) + 1
            max_freq = max(max_freq, window[s[end]])

            while (end - start + 1) - max_freq > k:
                window[s[start]] -= 1
                start += 1
                if window[s[start]] == 0:
                    del window[s[start]]
            
            res = max(res, end - start + 1)
        
        return res

# Use hashmap as window
# When length of hashmap exceeds k, remove from window until it doesn't
# Otherwise, keep adding to window and make sure to keep track of longest string