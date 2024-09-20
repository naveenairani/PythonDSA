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

q = Queue()
q.push(10)
q.push(20)
q.push(30)
print(q.contains(40))
q.push(10)
q.display()