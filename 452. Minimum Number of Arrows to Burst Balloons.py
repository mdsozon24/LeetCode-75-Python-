class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        p = sorted(p,key = lambda x:x[1])
        ans = 0
        i = 0
        while i<len(p):
            j = i+1
            while j<len(p) and p[j][0]<=p[i][1]:
                j+=1
            ans+=1
            i = j
        return ans