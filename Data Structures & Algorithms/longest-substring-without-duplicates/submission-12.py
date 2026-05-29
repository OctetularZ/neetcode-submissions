class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        start = 0
        longest_str = 0

        for end in range(len(s)):
            while s[end] in window:
                window.remove(s[start])
                start += 1
            window.add(s[end])
            longest_str = max(longest_str, end - start + 1)
        
        return longest_str