import math

class Hashtablelp:
    LINEAR_CONSTANT = 17
    def __init__(self,capacity=10):
        self.capacity = capacity
        self._adjust_capacity()
        self.table = [None] * self.capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity
    
    def _probe(self, x):
        return self.LINEAR_CONSTANT * x
    
    def _adjust_capacity(self):
        while math.gcd(self.LINEAR_CONSTANT, self.capacity) != 1:
            self.capacity += 1
    
    def insert(self, key, value):
        if self.size >= self.capacity:
            raise Exception("hashtable is full")
        index = self._hash(key)
        probe_count = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            
            probe_count += 1
            index = (index + self._probe(probe_count)) % self.capacity
        
        self.table[index] = (key, value)
        self.size += 1
    
    def search(self, key):
        index = self._hash(key)
        probe_count = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            probe_count += 1
            index = (index + self._probe(probe_count)) % self.capacity

        return None
    
    def delete(self, key):
        index = self._hash(key)
        probe_count = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1

                next_index = (index + self._probe(1)) % self.capacity
                while self.table[next_index] is not None:
                    next_key, next_value = self.table[index]
                    self.table[index] = None
                    self.size -=1
                    self.insert(next_key, next_value)
                    next_index = (index + self._probe(1)) % self.capacity
                return True
            probe_count += 1
            index = (index + self._probe(probe_count)) % self.capacity
        
        return False

    def __str__(self):
        display = []
        for i, value in enumerate(self.table):
            display.append(f"Key {i}: {value}")
        return "\n".join(display)