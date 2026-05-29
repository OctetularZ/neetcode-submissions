class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0

        for end in range(len(arr)):
            if (end - start + 1) == k + 1:
                a_abs = abs(arr[start] - x)
                b_abs = abs(arr[end] - x)
                if a_abs < b_abs or (a_abs == b_abs and arr[start] < arr[end]):
                    return arr[start : end]
                else:
                    start += 1
        
        return arr[len(arr) - k:]


# Sliding windows
# Since array is sorted, k closest integers to x should be contingous
# Keep adding to window until you get size of k.
# After above, If new element being added to window is closer to x, remove start of window
# If not, then return early with what we have. As if you keep going up, it'll get further away
# If abs(a-x) and abs(b-x) are equal, the negative number is closer to x.