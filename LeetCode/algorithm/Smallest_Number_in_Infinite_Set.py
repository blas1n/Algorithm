import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.curNum = 0
        self.pq = []

    def popSmallest(self) -> int:
        if self.pq:
            return heapq.heappop(self.pq)
        self.curNum += 1
        return self.curNum

    def addBack(self, num: int) -> None:
        if self.curNum >= num and num not in self.pq:
            heapq.heappush(self.pq, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)