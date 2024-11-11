class BinaryHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0
    
    def up(self, num: int):
        j = num // 2
        if j > 1:
            if self.heapList[num] < self.heapList[j]:
                self.heapList[num], self.heapList[j] = self.heapList[j], self.heapList[num]
                self.up(j)

    def down(self, i, n):
        j = i * 2
        if j <= n:
            if j < n:
                if self.heapList[j + 1] > self.heapList[j]:
                    j += 1
            if self.heapList[i] < self.heapList[j]:
                self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]
                self.down(j, n)

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.up(self.currentSize)

    def remove(self):
        if self.currentSize == 0:
            return None
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.down(1, self.currentSize)
        return retval

