class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            val = 0
            for n in piles:
                val += math.ceil(n / mid ) 
            if val <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
