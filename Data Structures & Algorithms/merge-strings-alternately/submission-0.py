class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ''
        idx = 0
        min_length = min(len(word1), len(word2))

        while idx < min_length:
            merged_string += word1[idx]
            merged_string += word2[idx]
            idx += 1
        
        if len(word1) > min_length:
            merged_string += word1[min_length:]
        if len(word2) > min_length:
            merged_string += word2[min_length:]
        
        return merged_string
        