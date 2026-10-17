class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(k):
            remaining = h
            
            for i in range(len(piles)):
                if k >= piles[i]:
                    remaining -= 1
                else: 
                    remaining -= (piles[i] + k - 1) // k
            
            if remaining >= 0:
                return True
            else:
                return False
        
        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
        