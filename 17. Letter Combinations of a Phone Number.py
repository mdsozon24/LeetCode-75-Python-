class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        def solve(i , s):
            if len(s)==len(digits):
                ans.append(s)
                return
            for c in d[digits[i]]:
                solve(i+1 , s+c)

        solve(0,'')
        return ans