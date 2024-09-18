class Node:
    def __init__(self, data, Prev=None, Next=None):
        self.data = data
        self.Prev = Prev
        self.Next = Next

    def __str__(self) -> str:
        return str(self.data)
    

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self.cNode = None

    def length(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def display():
        pass
    
    def addatFirst(self,elem):
        if self.isempty():
            self.head = self.tail = Node(elem)
        else:
            self.head.Prev = Node(elem,None, self.head)
            self.head = self.head.Prev
        self.size += 1

    def addatLast(self, elem):
        if self.isempty():
            self.tail =self.head = Node(elem)
        else:
            self.tail.Next = Node(elem,self.tail)
            self.tail = self.tail.Next
        self.size += 1

    def peekfirst(self):
        return self.head
    def peeklast(self):
        return self.tail
    def indexof(self, data):
        trav = self.head
        i = 0
        for _ in range(self.size):
            if trav.data == data:
                i += 1
                return trav.data, i
            else:
                trav = trav.Next
                i+=1

    def count(self, data):
        trav = self.head
        i = 0
        for _ in range(self.size):
            if trav.data == data:
                i += 1
                return trav.data, i
            else:
                trav = trav.Next

    def issorted(self):
        trav = self.head
        while trav.Next:
            if trav.data > trav.Next.data:
                return False
            else:
                trav = trav.Next
        return True

    def sort(self):
        trav = self.head
        while trav.Next:
            if trav.data > trav.Next.data:
                trav.data, trav.Next.data = trav.Next.data, trav.data
            trav = trav.Next


    def append(self, elem):
        if self.isempty():
            self.addatFirst(elem)
        else:
            self.addatLast(elem)

    def add(self, elem, index):
        if index<0 or index>self.size:
            raise IndexError("Index out of bound")
        new_node = Node(elem)
        
        if index == 0:
            new_node.Next = self.head
            self.head.Prev = new_node
            self.head = new_node
        elif index == self.size and self.tail.Next is None:
            new_node.Prev = self.tail
            self.tail.Next  =new_node
            self.tail  =new_node
        else:
            trav = self.head
            for _ in range(index):
                if trav is None:
                    raise IndexError("Index out of bound")
                trav = trav.Next

            if trav is None:
                raise IndexError("Index out of bound")
            new_node.Prev = trav.Prev
            new_node.Next = trav
            if trav.Prev is not None:
                trav.Prev.Next = new_node
            else:
                self.head = new_node
            
            trav.Prev = new_node
        self.size +=1
    
    def addafter(self, elem, index):
        if index > self.size or index< 0:
            raise IndexError("Index out of bound")
        new_node = Node(elem)
        if index == 0 and self.head is None:
            return "List is empty"
        if index == 0:
            new_node.Next = self.head.Next
            self.head.Next = new_node
            self.head.Prev = new_node.Prev
        elif index == self.size:
            new_node.Prev = self.tail.Next
            self.tail.Next = new_node.Prev
            self.tail.Next = new_node
        else:
            trav = self.head
            for _ in range(index):
                if trav is None:
                    raise IndexError("Index out of bound")
                trav = trav.Next
            new_node.Next = trav.Next
            trav.Next = new_node
            trav.Prev = new_node.Prev
        self.size += 1

    def addbefore(self, elem, index):
        if index>self.size or index<0:
            raise IndexError("Index out of bound")
        new_node = Node(elem)
        if index == 0 and index ==self.size:
            return "List is empty"
        if index == 0:
            new_node.Next = self.head
            self.head.Prev = new_node
            self.head = new_node
        elif index == self.size:
            new_node.Prev = self.tail.Prev
            new_node.Next = self.tail
            self.tail.Prev.Next = new_node
            self.tail.Prev = new_node

        else:
            trav = self.head
            for _ in range(index):
                if trav is None:
                    raise IndexError("Index out of Bound")
                trav = trav.Next
            new_node.Prev = trav.Prev
            new_node.Next = trav
            trav.Prev.Next = new_node
            trav.Prev = new_node
        
        self.size +=1
    
    def update(self, elem, index):
        if index>self.size or index<0:
            raise IndexError("Index out of bound")
        elif index == 0:
            self.head.data = elem
        elif index == self.size:
            self.tail.data = elem
        else:
            if index < self.size // 2:
                trav = self.head
                for _ in range(index):
                    trav = trav.Next
                trav.data = elem
            else:
                trav = self.tail
                for _ in range(self.size - 1, index, -1):
                    trav = trav.Prev
                trav.data = elem
        
            

    def removeFirst(self):
        if not self.isempty():
            self.head = self.head.Next
            self.head.Prev = None
        self.size -= 1

    def removeLast(self):
        if not self.isempty():
            self.tail = self.tail.Prev
            self.tail.Next = None
        self.size -= 1

    def removeNode(self,index):
        if index<0 or index>self.size:
            raise IndexError("Index out of bound")
        elif index == 0:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.Next
                self.head.Prev = None
        elif index == self.size-1:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.Prev
                self.tail.Next = None
        else:
            trav = self.head
            for _ in range(index):
                trav = trav.Next
            trav.Prev.Next = trav.Next
            trav.Next.Prev = trav.Prev
        self.size -= 1

    def removeObj(self,elem):
        trav = self.head
        while trav is not None:
            if trav.data == elem:
                if trav.Prev is None:
                    self.head = trav.Next
                    if self.head is not None:
                        self.head.Prev = None
                else:
                    trav.Prev.Next = trav.Next
            
                if trav.Next is None:
                    self.tail = trav.Prev
                    if self.tail is not None:
                        self.tail.Next = None
                else:
                    trav.Next.Prev = trav.Prev

                self.size -= 1
            
            trav = trav.Next
    def clear(self):
        self.head = None
        self.size = 0
        self.tail = None
            
    def search(self, elem):
        trav = self.head
        index = []
        for i in range(self.size):
            if trav.data == elem:
                trav = trav.Next
                index.append(i)
            elif trav.data != elem:
                trav = trav.Next
            else:
                return False
        return str(index)
    
    def getNode(self,index):
        if index >= self.size // 2:
            trav = self.tail
            for _ in range(self.size,index,-1):
                trav = trav.Prev
        elif index <= self.size // 2:    
            trav = self.head
            for _ in range(index):
                trav = trav.Next
        elif index<0 or index> self.size:
            raise IndexError("Index out of bound")
        elif index == self.size // 2:
            trav = self.head
            for _ in range(index):
                trav = trav.Next
        else:
            return False
        return trav

    def forward(self):
        if self.cNode is None:
            self.cNode = self.head
            data = self.cNode.data
            return data
        if self.cNode is not None:
            self.cNode = self.cNode.Next
            data = self.cNode.data
            return data
        else:
            raise StopIteration("End of elements")
    
    def backward(self):
        if self.cNode is None:
            self.cNode = self.tail
            data = self.cNode.data
            return data
        if self.cNode is not None:
            self.cNode = self.cNode.Prev
            data = self.cNode.data
            return data
        elif self.cNode.Prev is None:
            raise StopIteration("end of elements")
    
    def reverse(self):
        if self.head is None:
            return 
        else:
            next = self.head
            prev = self.tail
            for _ in range(self.size // 2):
                next.data, prev.data = prev.data, next.data
                prev = prev.Prev
                next = next.Next
    
    def merge(self, newlist):
        if not isinstance(newlist, DoublyLinkedList):
            raise TypeError("Argument is not a DoublyLinkedList")
        if self.head is None:
            self.head = newlist.head
            self.tail = newlist.tail
        else:
            self.tail.Next = newlist.head
            newlist.head.Prev = self.tail
            self.tail = newlist.tail
            self.size += newlist.size
        return self
    def __iter__(self):
        self._iter_node = self.head
        return self
    
    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        data = self._iter_node.data
        self._iter_node.data = self._iter_node.Next
        return data
    
    def __str__(self):
        element = []
        trav = self.head
        if self.size == 0:
            return '<-'+'NULL'+'->'
        while trav is not None:
            element.append(str(trav.data))
            trav = trav.Next
        return '<-'+'<->'.join(element)+'->'
