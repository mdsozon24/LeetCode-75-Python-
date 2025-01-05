class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0,1,1]
        if n<3:
            return l[n]
        for _ in range(3,n+1):
            l.append(l[-1]+l[-2]+l[-3])
        return l[-1]
        