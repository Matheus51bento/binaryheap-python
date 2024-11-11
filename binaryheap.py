import math


class BinaryHeap:
    def __init__(self):
        self.heapList = [1000000]
        self.currentSize = 0

    def up(self, index: int):

        j = index // 2
        if j >= 1:
            if self.heapList[index] > self.heapList[j]:
                self.heapList[index], self.heapList[j] = (
                    self.heapList[j],
                    self.heapList[index],
                )
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

    def arranjar(self, n):
        for i in range(n // 2, 0, -1):
            self.down(i, n)

    def ordenar(self, n=None):
        if n is None:
            n = self.currentSize
        self.arranjar(n)
        m = n
        for i in range(n, 1, -1):
            self.heapList[1], self.heapList[i] = self.heapList[i], self.heapList[1]
            m -= 1
            self.down(1, m)

    def get_high_priority(self):
        return self.heapList[1]

    def change_priority(self, index, new_priority):
        if index < 1 or index > self.currentSize:
            return

        old_priority = self.heapList[index]
        self.heapList[index] = new_priority

        if new_priority > old_priority:
            self.down(index, self.currentSize)
        else:
            self.up(index)

    def display_heap(self):
        print(self.heapList)

    def print_tree(self):

        depth = math.ceil(math.log2(self.currentSize + 1))

        index = 0
        for level in range(depth):
            level_count = 2**level

            leading_space = " " * (2 ** (depth - level) - 1)
            between_space = " " * (2 ** (depth - level + 1) - 1)

            line = leading_space
            line += between_space.join(
                f"{self.heapList[index + i + 1]:2}"
                for i in range(level_count)
                if index + i < self.currentSize
            )

            print(line)

            index += level_count
