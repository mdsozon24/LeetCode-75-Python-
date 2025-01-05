class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_candi = max(candies)
        for n in candies:
            ans.append((n+extraCandies)>=max_candi)
        return ans