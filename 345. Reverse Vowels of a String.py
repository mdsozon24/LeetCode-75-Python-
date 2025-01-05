class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = [c for c in s]
        vowel = []
        for c in arr:
            if c in "AEIOUaeiou":
                vowel.append(c)
        vowel = vowel[::-1]
        indx = 0
        for i in range(len(arr)):
            if arr[i] in "AEIOUaeiou":
                arr[i] = vowel[indx]
                indx+=1
        return "".join(arr)