class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            if (c&1):  
                if (not (a&1) and not (b&1)):
                    res+=1
            else:
                if (a&1) and (b&1):
                    res+=2
                elif (a&1) or (b&1):
                    res+=1
            c>>=1
            a>>=1
            b>>=1
        return res