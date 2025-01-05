class SmallestInfiniteSet:

    def __init__(self):
        self.arr = []
        self.x = 1

    def popSmallest(self) -> int:
        if self.arr:
            return heapq.heappop(self.arr)
        else:
            self.x+=1
            return self.x-1

    def addBack(self, num: int) -> None:
        if self.x > num and num not in self.arr:
            heapq.heappush(self.arr,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)