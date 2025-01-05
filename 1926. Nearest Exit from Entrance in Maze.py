class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ans = 0
        r = len(maze)
        c = len(maze[0])
        que = [entrance]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maze[entrance[0]][entrance[1]] = '+'
        while que:
            ans+=1
            for _ in range(len(que)):
                i,j = que.pop(0)
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c and maze[ni][nj] == '.':
                        if (ni==0 or ni==r-1 or nj==0 or nj==c-1) and [ni,nj]!=entrance:
                            return ans
                        maze[ni][nj] = '+'
                        que.append((ni, nj))
        return -1