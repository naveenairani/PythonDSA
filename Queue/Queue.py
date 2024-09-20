class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def isempty(self):
        return self.head is None

    def push(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
        
    def pop(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        else:
            popdata = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return popdata
    
    def contains(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            else:
                current = current.next
        return False
    
    def search(self, data):
        current = self.head
        index = []
        i = 0
        while current:
            if current.data == data:
                index.append(i)
            i += 1
            current = current.next
        return index
    
    def display(self):
        element = []
        current = self.head
        while current:
            element.append(str(current.data))
            current = current.next
        return print("<-".join(element))
    
    def enqueuefromlist(self, qlist):
        if self.head is None:
            for data in qlist:
                self.push(data)
        else:
            for data in qlist:
                self.push(data)

    def pop_multiple(self,n):
        for _ in range(n):
            self.pop()

    def rotate(self):
        current = self.head
        self.head = self.head.next
        if self.tail is not None:
            self.tail.next = current
            self.tail = current
            self.tail.next =None
    
    def multipeek(self, n):
        if n>self.length or n<0:
            raise IndexError("Index Out of boound")
        peek = Queue()
        current = self.head
        for _ in range(n):
            peek.push(current.data)
            current = current.next
        return peek
    
    def swap(self,first=0,second=1):
        if self.size() <2:
            raise IndexError("Queue is empty")
        if first == second:
            return "No operation required"
        if first > second:
            first, second = second, first

        firstnode = self.head
        secondnode = self.head.next
        if first ==0 and second==1:
            firstnode.next = secondnode.next
            secondnode.next = firstnode
            self.head = secondnode
        else:
            prevfirst = None
            current = self.head
            for _ in range(first):
                prevfirst = current
                current = current.next
            prevsecond = current
            currentnext = current.next
            for _ in range(second-first-1):
                prevsecond = currentnext
                currentnext = currentnext.next
            if current is None or currentnext is None:
                return "invalid"
            if prevfirst is not None:
                prevfirst.next = currentnext
            else:
                self.head = currentnext
            if prevsecond is not None:
                prevsecond.next = current
            else:
                self.head = current
            current.next, currentnext.next = currentnext.next, current.next

    def clear(self):
        self.head, self.tail, self.length= None, None,0
    
    def __len__(self):
        return self.length
    
    def size(self):
        return self.length
    
    def peek(self):
        return self.head
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
    def __iter__(self):
        data = self.current.data
        self._current = self._current.next
        return data
    def __str__(self):
        element = []
        current = self.head
        while current:
            element.append(str(current.data))
            current = current.next
        return "<-".join(element)
