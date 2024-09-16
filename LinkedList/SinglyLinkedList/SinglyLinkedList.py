class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.current = None

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def length(self):
        return self.size
    
    def addFirst(self,elem):
        self.head = Node(elem, self.head)
        self.size += 1
        if self.size == 1:
            self.current = self.head

    def addLast(self, elem):
        if self.is_empty():
            self.addFirst(elem)
        else:
            self.append(elem)
    
    def append(self,elem):
        if self.is_empty():
            self.addFirst(elem)
        else:
            new_node = Node(elem)
            if self.is_empty():
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node


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
            self.removeFirstNode()

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
                    
                i += 1
                prev = trav
                trav = trav.next
        self.size -= 1

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
    
    def bsearch(self, elem):
        pass
    
    def swapNode(self, nodeIndex1, nodeIndex2):
        if nodeIndex2 == nodeIndex1:
            return "no need to swap as index are same"
        if nodeIndex1> nodeIndex2:
            nodeIndex1, nodeIndex2 = nodeIndex2, nodeIndex1
        
        node1, node2, prev1, prev2 =  self.head, self.head, None, None

        for i in range(nodeIndex1):
            prev1 = node1
            node1 = node1.next
        
        for i in range(nodeIndex2):
            prev2 = node2
            node2 = node2.next
        
        if not node1 or not node2:
            return "out of indices"
        
        if prev1:
            prev1.next = node2
        else:
            self.head = node2
        
        if prev2:
            prev2.next = node1
        else:
            self.head = node1
        
        node1.next , node2.next = node2.next , node1.next

    def lSort(self):
        if self.is_empty():
            return False
        current = self.head
        while current is not None:
            trav = current.next
            while trav is not None:
                if current.data>trav.data:
                    temp = current.data
                    current.data = trav.data
                    trav.data = temp
                trav = trav.next
            current = current.next

    def clear(self):
        self.head = None
        self.size = 0

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
        self.head = prev

    def copy(self):
        if not self.head:
            return SinglyLinkedList()
        new_list = SinglyLinkedList()
        trav =self.head
        while trav is not None:
            new_list.append(trav.data)
            trav = trav.next
        return new_list
    
    def merge(self, list2):
        mergedlist = SinglyLinkedList()
        list1 = self.head
        while list1 is not None:
            mergedlist.append(list1.data)
            list1 = list1.next
        list2 = list2.head
        while list2 is not None:
            mergedlist.append(list2.data)
            list2 = list2.next
        return mergedlist

    def detectLoop(self):
        slow ,fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
            else:
                return False


    def traverse(self):
        if self.current is None:
            print("List is empty")
        data = self.current.data
        self.current = self.current.next
        return data
    
    def middleNode(self):
        middle = self.size // 2
        trav = self.head
        for _ in range(middle):
            trav = trav.next
        return trav.data, middle

    def nthNode(self, node):
        if node>self.size and node<0:
            raise IndexError("Index out of bound")
        fast = slow = self.head
        for _ in range(node):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.data

    def contains(self, elem):
        return self.index_of(elem) != -1
    
    def __iter__(self):
        self._iter_node = self.head
        return self
    
    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        data = self._iter_node.data
        self._iter_node = self._iter_node.next
        return data
    
    def __str__(self):
        element = []
        trav = self.head
        if self.head is None:
            return "NULL"
        while trav is not None:
            element.append(str(trav.data))
            trav = trav.next
        return ''+'->'.join(element)+''