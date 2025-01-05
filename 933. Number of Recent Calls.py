class RecentCounter:

    def __init__(self):
        self.que = []

    def ping(self, t: int) -> int:
        if not self.que :
            self.que.append(t)
            return 1
        else:
            if t<3000 :
                self.que.append(t)
                return len(self.que)
            else:
                x = t-3000
                while self.que and self.que[0] < x:
                    self.que.pop(0)
                self.que.append(t)
                return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)