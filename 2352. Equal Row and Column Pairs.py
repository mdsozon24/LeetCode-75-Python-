class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        my_grid = list(zip(*grid))
        ans = 0
        for row in grid:
            for column in my_grid:
                if row == list(column):
                    ans+=1
        return ans