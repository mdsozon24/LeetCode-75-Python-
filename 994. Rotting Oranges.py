class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        time,frs = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    frs+=1
                if grid[i][j]==2:
                    que.append([i,j])
        dis = [[0,1],[0,-1],[1,0],[-1,0]]
        while que and frs > 0:
            for _ in range(len(que)):
                r,c = que.pop(0)
                for i,j in dis:
                    row,col = r+i,c+j
                    if (row < 0 or row == len(grid) or 
                    col < 0 or col == len(grid[0]) or 
                    grid[row][col]!=1):
                        continue
                    grid[row][col] = 2
                    que.append([row,col])
                    frs-=1
            time+=1
        return time if frs==0 else -1