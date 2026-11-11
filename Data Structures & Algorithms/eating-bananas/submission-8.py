class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while (l <= r):
            
            t = 0
            mid = l + (r - l) // 2

            for p in piles:
                t += (p // mid) + 1 * (p % mid != 0)
            
            if t > h:
                l = mid + 1
            elif t <= h:
                r = mid - 1
        

        return l


    