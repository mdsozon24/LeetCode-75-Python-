class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        s =""
        n=len(w1)
        m=len(w2)
        i=0
        while i<n or i<m:
            if i<n:
                s+=w1[i]
            if i<m:
                s+=w2[i]
            i+=1
        return s