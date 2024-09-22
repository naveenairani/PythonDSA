class Binaryheap:
    def __init__(self, elem=None):
        if elem is None:
            elem = []
        self.heap = elem
        self.index = 0
        self.heapsize = len(elem)
        if self.heapsize>0:
            self.heapify()
    
    def  is_empty(self):
        return self.heapsize == 0
    
    def size(self):
        return self.heapsize
    
    def clear(self):
        self.heap.clear()
        self.heapsize = 0
    
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]
    
    def poll(self):
        if self.is_empty():
            raise IndexError("List is empty")
        root = self.heap[0]
        self.heap[0] = self.heap[self.heapsize - 1]
        self.heap.pop()
        self.heapsize -= 1
        self.sink(0)
        return root
    
    def contains(self, elem):
        return elem in self.heap
    
    def add(self, elem):
        if elem is None:
            raise ValueError("Element can not be None")
        if self.heapsize< len(self.heap):
            self.heap.insert(self.heapsize, elem)
        else:
            self.heap.append(elem)
        self.swim(self.heapsize)
        self.heapsize += 1
    
    def less(self, i, j):
        return self.heap[i]<self.heap[j]
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def swim(self, k):
        parent  = (k-1)//2
        while k>0 and self.less(k, parent):
            self.swap(k, parent)
            k = parent
            parent  = (k-1)//2

    def sink(self,k):
        while True:
            left  = 2*k+1
            right = 2*k+2
            smallest = k
            if left < self.heapsize and self.less(left, smallest):
                smallest = left
            if right > self.heapsize and self.less(right, smallest):
                smallest = right
            if smallest == k:
                break
        self.swap(k, smallest)
        k = smallest

    def heapify(self):
        for i in range((self.heapsize-1)//2,-1,-1):
            self.sink(i)

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index< self.heapsize:
            result = self.heap[self.index]
            self.index +=1
            return result
        else:
            raise StopIteration
    
    def __str__(self):
        if self.is_empty():
            return "Heap is empty"
        output = []
        level = 0
        element_in_level = 1

        while (level_start := (1<<level)-1) < self.heapsize:
            level_end = min(self.heapsize, level_start+ element_in_level)
            output.append(" ".join(str(self.heap[i]) for i in range(level_start, level_end)))
            if level_end == self.heapsize:
                break
            level += 1
            element_in_level *= 2
        return "\n".join(output)
