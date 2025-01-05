class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(list)
        for i in range(len(equations)):
            dic[equations[i][0]].append((equations[i][1],values[i]))
            dic[equations[i][1]].append((equations[i][0],1/values[i]))
        def dfs(src,trgt,ans,visit):
            if src not in dic or trgt not in dic:
                return -1.0
            if src in visit:
                return -1.0
            visit.add(src)
            if src==trgt:
                return (ans)
            for u,v in dic[src]:
                if u not in visit:
                    val = dfs(u,trgt,ans*v,visit)
                    if val != -1:
                        return val
            return -1.0
        res = []
        for a,b in queries:
            visit = set()
            res.append(dfs(a,b,1,visit))
        return res