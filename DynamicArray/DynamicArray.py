class DynamicArray:
    def __init__(self,capacity=16):
        if capacity<0:
            raise ValueError(f"Illegal Capacity:{capacity}")
        self.capacity = capacity
        self.len = 0
        self.arr = [None] * capacity

    def size(self):
        return self.len
    
    def is_empty(self):
        return self.size()==0
    
    def get(self, index):
        if index >= self.len or index <0:
            raise IndexError("Index out of bound")
        return self.arr[index]
    
    def set(self, index, value):
        if index >= self.len or index < 0:
            raise IndexError("Index out of bound")
        self.arr[index] = value
    
    def clear(self):
        for i in range(self.len):
            self.arr[i] = None
        self.len = 0

    def append(self,value):
        if self.len + 1 >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2

                new_arr = [None]*self.capacity
                for i in range(self.len):
                    new_arr[i] = self.arr[i]
                self.arr = new_arr
        self.arr[self.len] = value
        self.len += 1

    def add(self, index, value):
        if index > self.len or index < 0:
            raise IndexError("Index out of bound")
        
        if self.len + 1> self.capacity:
            self.capacity = max(1, self.capacity *2)
            new_arr = [None] * self.capacity
            for i in range (self.len):
                new_arr = self.arr[i]
            self.arr = new_arr

        for i in range(self.len, index, -1):
            self.arr[i] = self.arr[i - 1]
        
        self.arr[index] = value
        self.len += 1
    
    def remove(self, index):
        if index >= self.len or index < 0:
            raise IndexError("Index out of bound")
        data = self.arr[index]
        new_arr = [None]*(self.len -1)
        for i, j in zip(range(self.len), range(self.len - 1)):
            if i == index:
                j -= 1
            else:
                new_arr[j] = self.arr[i]
        self.arr = new_arr
        self.capacity = self.len - 1
        self.len -= 1
        return data
    
    def delete(self, obj):
        index = self.index_of(obj)
        if index == -1:
            return False
        self.remove_at(index)
        return True
    
    def index_of(self, obj):
        for i in range(self.len):
            if obj is None:
                if self.arr[i] is None:
                    return i
            elif obj == self.arr[i]:
                return i
        return -1
    
    def InsertionSort(self):
        for i in range(self.len):
            key = self.arr[i]
            j = i -1
            while j>=0 and self.arr[j]>key:
                self.arr[j+1] = self.arr[j]
                j = j - 1
                self.arr[j+1] = key
    
    def SelectionSort(self):
        for i in range(self.len-1):
            min = i
            for j in range(i+1,self.len):
                if self.arr[min] < self.arr[j]:
                    min = j
            
                self.arr[min], self.arr[j] = self.arr[j], self.arr[min]

    def BubbleSort(self):
        for i in range(self.len-1):
            for j in range(self.len - i -1):
                if self.arr[j]> self.arr[j+1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = temp

    
    def contains(self, obj):
        return self.index_of(obj) != -1
    
    def __iter__(slef):
        self._index = 0
        return self
    
    def __next__(self):
        if self._index < self.len:
            result = self.arr[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
    
    def __str__(self):
        if self.len == 0:
            return "[]"
        else:
            return "[" + ",".join(map(str, self.arr[:self.len]))+']'

