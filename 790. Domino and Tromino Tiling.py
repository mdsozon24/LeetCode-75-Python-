class Solution:
    def numTilings(self, n: int) -> int:
        ans = [0,1,2,5]
        for i in range(4,n+1):
            ans.append(((2*ans[i-1])+ans[i-3])%(10**9+7))
        return ans[n]