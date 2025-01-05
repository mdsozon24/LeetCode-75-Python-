class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        que = set(val for val in rooms[0])
        visited.add(0)
        while len(que)!=0:
            val = que.pop()
            visited.add(val)
            for x in rooms[val]:
                if (x not in que) and (x not in visited):
                    que.add(x)
        return len(visited)==len(rooms)