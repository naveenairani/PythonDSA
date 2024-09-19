class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def push(self, data):
        newnode  = Node(data)
        newnode.next = self.top
        self.top = newnode
    
    def pop(self):
        if self.isempty():
            raise IndexError("Stack is empty")
        popnode = self.top.data
        self.top = self.top.next
        return popnode
    
    def isempty(self):
        return self.top is None
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.top
    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
            
        return count
    def clear(self):
        self.top = None

    def contain(self, data):
        current = self.top
        while current:
            if current.data == data:
                return True
            else:
                current = current.next
        return False
    
    def tolist(self):
        current = self.top
        tolist = []
        while current:
            tolist.append(current.data)
            current = current.next
        return tolist
    
    def fromlist(self, userlist):
        for item in reversed(userlist):
            self.push(item)
    def reverse(self):
        current = self.top
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.top = prev
            
        

    def __iter__(self):
        self._current = self.top
        return self
    
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            value = self._current
            self._current = self._current.next
            return value

    def __str__(self):
        element = []
        current = self.top
        while current:
            element.append(str(current.data))
            current = current.next
        return '['+','.join(element)+']'
stack = Stack()

stack.push(10)
stack.push(11)
print(stack.pop())
stack.push(100)
print(stack.size())
print(stack)
stack.clear()
print(stack)
list1 = [10,20,30,10,50,'naveen']
stack.fromlist(list1)
print(stack)
newlist = stack.tolist()
print(newlist)
stack.reverse()
print(stack)