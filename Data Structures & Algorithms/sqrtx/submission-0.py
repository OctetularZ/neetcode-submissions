class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        left, right = 0, x
        res = 0

        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
                res = mid
            else:
                return mid
        
        return res

