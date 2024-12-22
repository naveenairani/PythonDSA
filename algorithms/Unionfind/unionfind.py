class unionfind:
    def __init__(self, size):
        if size<=0:
            raise ValueError("Size must be positive")
        self.size = size
        self.numComponent = size
        self.sz = [1]*size
        self.id = list(range(size))
        self.rank = [1]*size
    
    def find(self,p):
        root = p
        while root != self.id[root]:
            root = self.id[root]
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next

        return root
    
    def connected(self, p,q):
        return self.find(p)==self.find(q)
    
    def componentSize(self, p):
        return self.sz[self.find(p)]
    
    def components(self):
        return self.numComponent
    
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        if root1 == root2:
            return
        
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        
        self.numComponent -= 1
    
    def unify_by_rank(self, p, q):
        root1 = self.find(p)
        root2 = self.fing(q)

        if root1 == root2:
            return
        
        if self.rank[root1]< self.rank[root2]:
            self.id[root1] = root2
        elif self.rank[root1]> self.rank[root2]:
            self.id[root2] = root1
        else:
            self.id[root2] = root1
            self.rank[root1] += 1
        self.numComponent += 1
    
    def find_with_compression(self, p):
        root = p
        steps = 0
        while root!=self.id[root]:
            root = self.id[root]
        
        while p!=self.id[root]:
            next = self.id[p]
            self.id[p] = root
            p = next
            steps += 1
        
        return root, steps

    def maximun_depth(self):
        max_depth = 0
        max_depth_component = None
        for i in range(self.size):
            root = self.find(i)
            depth = 0
            temp = i
            while temp != root:
                temp = self.id[root]
                depth += 1

    def find_small_element(self, p):
        root = self.find(p)
        min = root
        for i in range(self.size):
            if self.find(i) == root and i < min:
                min = i 
        return min

    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current<self.size:
            item = self.size
            self.current += 1
            return item
        else:
            raise StopIteration
    
    def __str__(self):
        return f"UnionFind=(size={self.size}, components={self.numComponent}, id's{self.id}, size={self.size})"
