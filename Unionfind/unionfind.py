class unionfind:
    def __init__(self, size):
        if size<=0:
            raise ValueError("Size must be positive")
        self.size = size
        self.numComponent = size
        self.sz = [1]*size
        self.id = list(range(size))
    
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