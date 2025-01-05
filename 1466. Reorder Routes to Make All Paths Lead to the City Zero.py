class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        dic = defaultdict(list)
        for a,b in connections:
            dic[a].append((b,True))
            dic[b].append((a,False))
        stk = [0]
        visit = set()
        while stk:
            val = stk.pop()
            visit.add(val)
            for first,last in dic[val]:
                if first not in visit:
                    stk.append(first)
                    if last:
                        ans+=1
        return ans