class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        i,j = 0,0
        s = ''
        while j<len(chars):
            while j<len(chars) and chars[i]==chars[j]:
                j+=1

            s+=chars[i]
            if j-i>1:
                s+=str(j-i)
            i = j
            
        for k in range(len(s)):
            chars[k] = s[k]
            
        return len(s)