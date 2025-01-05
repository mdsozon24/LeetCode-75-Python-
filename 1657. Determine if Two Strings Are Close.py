class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1)!=len(w2):
            return False
        d={}
        e={}
        for i in range(len(w1)):
            if not w1[i] in w2:
                return False
            d[w1[i]]=d.get(w1[i],0)+1     
            e[w2[i]]=e.get(w2[i],0)+1
        return sorted(list(d.values()))==sorted(list(e.values()))        