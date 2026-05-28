from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        state = {}
        s1_state = Counter(s1)

        for end in range(len(s2)):
            state[s2[end]] = state.get(s2[end], 0) + 1
            
            if end - start + 1 == len(s1):
                print(state)
                if state == s1_state:
                    return True
                
                state[s2[start]] -= 1
                if state[s2[start]] == 0:
                    del state[s2[start]]
                start += 1
        
        return False


# Fixed sliding window through s2, length of s1
# If window contains all letters of s1, then it is a valid permutation (return True), otherwise return False
