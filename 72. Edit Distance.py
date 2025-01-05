class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        def solve(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            if word1[i]==word2[j]:
                return solve(i+1,j+1)
            if dp[i][j]!=-1:
                return dp[i][j]
            else:
                delete = 1+solve(i+1,j)
                insert = 1+solve(i,j+1)
                replace = 1+solve(i+1,j+1)

            dp[i][j] = min(delete,insert,replace)
            return dp[i][j]
        return solve(0,0)