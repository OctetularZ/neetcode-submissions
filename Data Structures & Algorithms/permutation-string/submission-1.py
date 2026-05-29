from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        s1_count = Counter(s1)
        start = 0
        n1 = len(s1)
        n2 = len(s2)

        for end in range(n2):
            window[s2[end]] = window.get(s2[end], 0) + 1

            if (end - start + 1) == n1:
                print(window)
                if window == s1_count:
                    return True
                else:
                    window[s2[start]] -= 1
                    if window[s2[start]] == 0:
                        del window[s2[start]]
                    start += 1

        return False
