# DoublyLinkedList Python Implementation

This project provides a custom implementation of a Doubly Linked List in Python. The `DoublyLinkedList` class contains various methods for manipulating the list, including adding, removing, searching, and updating nodes. Each node in the list has references to both the previous and next nodes, allowing for efficient traversal in both directions.

## Features

- **Add Operations**
  - `addatFirst(elem)` - Add a node at the beginning.
  - `addatLast(elem)` - Add a node at the end.
  - `add(elem, index)` - Add a node at a specific index.
  - `addafter(elem, index)` - Add a node after a specific index.
  - `addbefore(elem, index)` - Add a node before a specific index.
  - `append(elem)` - Append a node to the list.

- **Remove Operations**
  - `removeFirst()` - Remove the first node.
  - `removeLast()` - Remove the last node.
  - `removeNode(index)` - Remove a node by index.
  - `removeObj(elem)` - Remove a node by value.
  - `clear()` - Remove all nodes from the list.

- **Update Operation**
  - `update(elem, index)` - Update a node's data at a specific index.

- **Traversal Operations**
  - `forward()` - Move forward through the list.
  - `backward()` - Move backward through the list.

- **Sorting**
  - `issorted()` - Check if the list is sorted.
  - `sort()` - Sort the list.

- **Merging**
  - `merge(newlist)` - Merge another doubly linked list into the current list.

- **Search and Retrieve**
  - `search(elem)` - Search for an element and return the indices.
  - `indexof(data)` - Find the index of an element.
  - `count(data)` - Count occurrences of an element.
  - `getNode(index)` - Get the node at a specific index.

- **Helper Methods**
  - `length()` - Get the size of the list.
  - `isempty()` - Check if the list is empty.
  - `peekfirst()` - View the first node.
  - `peeklast()` - View the last node.
  - `reverse()` - Reverse the elements of the list.

## Installation

To use this class, simply copy the Python code into your project and instantiate the `DoublyLinkedList` class.

## Usage

```python
# Import or define the class in your project
dll = DoublyLinkedList()

# Add elements to the list
dll.addatFirst(10)
dll.addatLast(20)
dll.add(15, 1)

# Traverse the list
for node in dll:
    print(node)

# Remove elements
dll.removeFirst()
dll.removeNode(1)

# Search for elements
print(dll.search(20))  # Output: indices where 20 is found

# Reverse the list
dll.reverse()

# Merge with another list
dll2 = DoublyLinkedList()
dll2.append(50)
dll.merge(dll2)

# Print the list
print(dll)
