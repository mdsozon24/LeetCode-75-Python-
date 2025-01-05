class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(arr,v):
            visit[v] = True
            for n in arr:
                if not visit[n]:
                    dfs(dic[n],n)
        n = len(isConnected)
        visit = [False]*n
        dic = defaultdict(list)
        ans = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    dic[i].append(j)
                    dic[j].append(i)
        for i in range(n):
            if not visit[i]:
                dfs(dic[i],i)
                ans+=1
        return ans