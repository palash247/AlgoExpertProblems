class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.remove(node)
            self.head = node

    def setTail(self, node):
        # Write your code here.
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.remove(node)
            self.tail = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if node is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            self.removeBindings(nodeToInsert)
        elif node is self.head:
            self.remove(nodeToInsert)
            nodeToInsert.next = node
            node.prev = nodeToInsert
            self.head = nodeToInsert
        else:
            self.remove(nodeToInsert)
            nodeToInsert.next = node
            nodeToInsert.prev = node.prev
            node.prev = nodeToInsert
            nodeToInsert.prev.next = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if node is None:
            self.head = nodeToInsert
            self.tail = nodeToInsert
            self.removeBindings(nodeToInsert)
        elif node is self.tail:
            self.remove(nodeToInsert)
            node.next = nodeToInsert
            nodeToInsert.prev = node
            self.tail = nodeToInsert
        else:
            self.remove(nodeToInsert)
            nodeToInsert.prev = node
            nodeToInsert.next = node.next
            nodeToInsert.next.prev = nodeToInsert
            node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        # position counting is from 1
        current = self.head
        if not current:
            self.setHead(nodeToInsert)
        else:
            while position != 0 and current.next is not None:
                current = current.next
                position -= 1
                if position == 0:
                    self.insertBefore(current.prev, nodeToInsert)
                elif position == 1:
                    self.insertBefore(current, nodeToInsert)
                else:
                    self.insertAfter(current, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        current = self.head
        while current is not None:
            back = current.next
            if current.value == value:
                self.remove(current)
            current = back

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.removeBindings(node)

    def containsNodeWithValue(self, value):
        # Write your code here.
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def removeBindings(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
