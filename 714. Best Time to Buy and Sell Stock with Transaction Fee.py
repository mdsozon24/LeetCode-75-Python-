class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        def solve(i,buying):
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            relax = solve(i+1,buying)
            if buying:
                buy = solve(i+1,not buying)-prices[i]
                dp[(i,buying)] = max(relax,buy)
            else:
                sell = solve(i+1,not buying)+prices[i]-fee
                dp[(i,buying)] = max(relax,sell)
            return dp[(i,buying)]
        return solve(0,True)