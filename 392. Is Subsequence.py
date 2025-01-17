class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i<len(s) and j<len(t):
            if j>= len(t):
                return False
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)