class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()
        res = []
        for a in spells:
            i,j=0,n-1
            while i<=j:
                mid = (i+j)//2
                if potions[mid]*a < success:
                    i = mid+1
                else:
                    j = mid-1
            res.append(n-i)
        return res    