class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solution(i,j):
            if i==(m-1) and j==(n-1):
                return 1
            if i>=m or j>=n:
                return 0
            if arr[i][j]!= 0:
                return arr[i][j]
            right = solution(i,j+1)
            down = solution(i+1,j)
            arr[i][j] = right + down
            return arr[i][j]

        arr = [[0]*n for _ in range(m)]
        return solution(0,0)