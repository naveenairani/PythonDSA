class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def length(self):
        return self.size
    
    def addFirst(self,elem):
        self.head = Node(elem, self.head)
        self.size += 1

    def addLast(self, elem):
        if self.is_empty():
            self.addFirst(elem)
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = Node(elem)
            self.size += 1
    
    def append(self,elem):
        if self.is_empty():
            self.add_first(elem)
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = Node(elem)
            self.size += 1

    def set(self, elem, index):
        if index<0 or index>self.size:
            raise IndexError("Index out of bound")
        trav = self.head
        i = 0
        while trav is not None:
            if i == index:
                trav.data = elem
            i += 1
            trav = trav.next
        self.size += 1

    def addAfterNode(self, elem, index):
        if index<0 or index>self.size:
            raise IndexError("Index out of bound")
        trav = self.head
        i = 0
        while trav is not None:
            if i == index:
                new_node = Node(elem)
                new_node.next = trav.next
                trav.next = new_node
                self.size += 1
            i += 1
            trav = trav.next


    def removeFirstNode(self):
        if self.is_empty():
            raise RuntimeError("Empty List")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def removeLastNode(self):
        if self.is_empty():
            raise RuntimeError("Empty List")
        if self.size == 1:
            self.remove_first()

        prev = None
        trav = self.head
        while trav.next is not None:
            prev = trav
            trav = trav.next
        prev.next = None
        self.size -= 1
        return trav.data
    
    def removeData(self, elem):
        if self.head is None:
            return
        while self.head is not None and self.head.data == elem:
            self.removeFirstNode()
        trav = self.head.next
        prev = self.head
        while trav is not None:
            if trav.data == elem:
                prev.next = trav.next
                self.size -= 1
            else:
                prev = trav
            trav = trav.next
            
    
    def removeNodeIndex(self, index):
        if index<0 or index>self.size:
            raise IndexError("Index out of bound")
        trav = self.head
        if self.size == index == 0:
            self.removeFirstNode()
        elif self.size == index:
            self.removeLastNode()
        else:
            trav = self.head
            prev = None
            i = 0
            while trav is not None:
                if i == index:
                    prev.next = trav.next
                    trav = prev
                    self.size -= 1
                i += 1
                prev = trav
                trav = trav.next

    def index_of(self, elem):
        index = 0
        trav = self.head
        while trav is not None:
            if trav.data == elem:
                return index
            trav = trav.next
            index +=1
        return -1
    
    def printList(self):
        elements = []
        trav = self.head
        while trav is not None:
            elements.append(trav.data)
            trav = trav.next
        return elements
    
    def lSearch(self, elem):
        trav = self.head
        index = []
        i = 0
        while trav is not None:
            if trav.data == elem:
                index.append(i)
            i += 1
            trav = trav.next
        return index
    
    def bSearch(self, elem):
        if self.is_empty():
            return False
    
    def swap(self, node1, node2):
        tmp = node1
        node1 = node2
        node2 = tmp

    def lSort(self):
        sort_head = self.head
        current = self.head
        while current is not None:
            next_node = current
            if sort_head is None or sort_head.data>=current.data:
                current.next = sort_head
            else:
                while current is not None and sort_head.data<=current.data:
                    current = current.next
                sort_head.next = current.next
                current.next  = sort_head
            current = sort_head
        return sort_head




    def contains(self, elem):
        return self.index_of(elem) != -1
    
    def __iter__(self):
        self._iter_node = self.head
        return self
    
    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        data = self._iter_node.data
        self._iter_node.data = self._iter_node.next
        return data
    
    def __str__(self):
        element = []
        trav = self.head
        while trav is not None:
            element.append(str(trav.data))
            trav = trav.next
        return ''+'->'.join(element)+''
    
