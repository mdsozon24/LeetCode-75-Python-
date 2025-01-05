class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        x = 0
        vowel = {'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowel:
                x+=1
        res = x
        for i in range(k,len(s)):
            if s[i] in vowel:
                x+=1
            if s[i-k] in vowel:
                x-=1
            res = max(x,res)
        return res