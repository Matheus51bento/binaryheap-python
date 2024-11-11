from binaryheap import BinaryHeap
import random

if __name__ == '__main__':
    heap = BinaryHeap()
    # heap.insert(95)
    # heap.insert(60)
    # heap.insert(78)
    # heap.insert(39)
    # heap.insert(28)
    # heap.insert(66)
    # heap.insert(70)

    for i in range(30):
        heap.insert(random.randint(1, 100))

    heap.arranjar(30)

    heap.display_heap()

    heap.print_tree()

    heap.ordenar(30)

    heap.display_heap()

    heap.print_tree()
