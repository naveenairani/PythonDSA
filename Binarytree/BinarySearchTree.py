class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return self.data

class BST:
    def __init__(self) -> None:
        self.root = None
        self.nodeCount = 0
    
    def size(self):
        return self.nodeCount
    
    def isempty(self):
        return self.size() == 0
    
    def _contains(self, node, elem):
        if node is None:
            return False
        if elem < node.data:
            return self._contains(node.left, elem)
        elif elem > node.data:
            return self._contains(node.right, elem)
        else:
            return True
    
    def contains(self, elem):
        return self._contains(self.root,elem)

    def add(self, elem):
        if self.contains(elem):
            return False
        else:
            self.root = self._add(self.root, elem)
            self.nodeCount += 1
            return True
    
    def _add(self, node, elem):
        if node is None:
            return Node(elem)
        if elem < node.data:
            node.left = self._add(node.left, elem)
        else:
            node.right = self._add(node.right, elem)
        return node
    
    def remove(self, elem):
        pass

    def _remove(self, node, elem):
        if node is None:
            return None
        if elem < node.data:
            node.left = self._remove(node.left, elem)
        elif elem > node.data:
            node.right = self._remove(node.right, elem)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.data = min_node.data
                node.right = self._remove(node.right, min_node.data)
        return node
     
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return int(max(self._height(node.left),self._height(node.right))) + 1
    
    def pre_order_traversal(self):
        result = []
        self._pre_order_traversal(self.root, result)
        return result

    def _pre_order_traversal(self, node, result):
        if node is not None:
            result.append(node.data)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)
    
    def in_order_traversal(self):
        result = []
        self._in_order_traversal(self.root,result)
        return result
    
    def _in_order_traversal(self, node, result):
        if node is not None:
            self._in_order_traversal(node.left, result)
            result.append(node.data)
            self._in_order_traversal(node.right, result)
    
    def post_order_traversal(self):
        result = []
        self._post_order_traversal(self.root, result)
        return result
    
    def _post_order_traversal(self, node, result):
        if node is not None:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.data)
    
    def valid_bst(self):
        return self._valid_bst(self.root, float('-inf'), float('inf'))

    def _valid_bst(self, node, min, max):
        if node is None:
            return True
        if not (min<node.data<max):
            return False
        return (self._valid_bst(node.left, min, node.data) and
                self._valid_bst(node.right, node.data, max))

    def __str__(self):
        if self.root is None:
            return 'Tree is empty'
        
        levels = []
        self._print_level(self.root, 0, levels)
        
        result = ""
        for i, level in enumerate(levels):
            result += f"Level {i}: {' '.join(map(str, level))}\n"
        
        return result

    def _print_level(self, node, level, levels):
        if node is None:
            return
        
        if len(levels) == level:
            levels.append([])
        
        levels[level].append(node.data)
        
        self._print_level(node.left, level + 1, levels)
        self._print_level(node.right, level + 1, levels)
