class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)
    
    def __eq__(self, other) -> bool:
        return self.hash == other.hash and self.key == other.key
    
    def __str__(self) -> str:
        return f"{self.key} => {self.value}"
    
class HashTableSeperatingChaninig:
    DEFAULT_CAPACITY = 3
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self, capacity = DEFAULT_CAPACITY, maxloadfactor = DEFAULT_LOAD_FACTOR) -> None:
        if capacity < 0:
            raise ValueError("Error in capacity")
        if maxloadfactor<= 0 or maxloadfactor == float('NaN') or maxloadfactor == float('inf'):
            raise ValueError("Error in Maxloadfactor")
        
        self.capacity = max(capacity, self.DEFAULT_CAPACITY)
        self.maxloadfactor = maxloadfactor
        self.threshold = int(self.capacity * self.maxloadfactor)
        self.size = 0
        self.table = [None] * self.capacity
    
    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0
    
    def _normalize_index(self, key_hash):
        return key_hash & 0x7FFFFFFF % self.capacity
    
    def put(self, key, value):
        new_entry = Entry(key, value)
        bucket_index = self._normalize_index(hash(new_entry.key))
        bucket = self.table[bucket_index]

        if bucket is None:
            self.table[bucket_index] = bucket = []
        
        for entry in bucket:
            if entry.key == key:
                old_value = entry.value
                entry.value = value
                return old_value
        
        bucket.append(new_entry)
        self.size += 1
        if self.size > self.threshold:
            self._resize_table()
    
    def get(self, key):
        bucket_index = self._normalize_index(hash(key))
        bucket = self.table[bucket_index]

        if bucket is None:
            return None
        
        for entry in bucket:
            if entry.key == key:
                return entry.value
        
        return None
    
    def _resize_table(self):
        new_capacity  = self.capacity * 2
        new_table = [None] * new_capacity

        for bucket in self.table:
            if bucket:
                for entry in bucket:
                    new_bucket_index = entry.hash % new_capacity
                    if new_table[new_bucket_index] is None:
                        new_table[new_bucket_index] = []
                    new_table[new_bucket_index].append(entry)
        
        self.capacity = new_capacity
        self.table = new_table
        self.threshold = int(self.capacity * self.maxloadfactor)
    
    def remove(self, key):
        bucket_index = self._normalize_index(hash(key))
        bucket = self.table[bucket_index]

        if bucket is None:
            return None

        for i,entry in enumerate(bucket):
            if entry.key == key:
                removed_value = entry.value
                bucket.pop(i)
                self.size -= 1
                return removed_value
        
        return None

    def keys(self):
        key_list = []
        for bucket in self.table:
            if bucket:
                for entry in bucket:
                    key_list.append(entry.key)
        return key_list

    def merge(self, other_table=None):
        if other_table is None:
            raise ValueError
        for key in other_table:
            self.put(key, other_table.get(key))
    
    def isFull(self):
        return self.size >= self.threshold
    
    def entries(self):
        entry = {}
        for bucket in self.table:
            if bucket:
                for entries in bucket:
                    entry[entries.value] = entries.key
        return entry
    
    def loadfactor(self):
        return self.size / self.capacity
    
    def get_max_key(self):
        max_key = None
        for key in self:
            if max_key is None or max_key > key:
                max_key = key
        return key
    
    def get_min_key(self):
        min_key = None
        for key in self:
            if min_key is None or min_key<key:
                min_key = key
        return min_key
    
    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                bucket_str = f"Bucket {i}:"+"=>".join([f'{entry.key}=>{entry.value}' for entry in bucket])
                result.append(bucket_str)
            else:
                result.append(f'Bucket {i}:None')
        return '\n'.join(result)
