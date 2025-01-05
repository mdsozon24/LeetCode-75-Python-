# from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m={}
        for i in arr:
            m[i]=m.get(i,0)+1
        # m = Counter(arr)
        l=list(m.values())
        if len(l)==len(set(l)):
            return True
        else:
            return False