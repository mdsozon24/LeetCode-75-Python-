class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def solve(s,k,n,arr,sm):
            if len(arr)==k and sm==n:
                ans.append(arr[:])
                return
            if sm>n or len(arr)>k:
                return
            for i in range(s,10):
                solve(i+1,k,n,arr+[i],sm+i)
        solve(1,k,n,[],0)
        return ans