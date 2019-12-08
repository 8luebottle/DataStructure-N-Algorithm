from node import Node

class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    # Start from Head print out each node's value
    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.pointer
        print()

    # Base to Prev Node | Delete Node
    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    # Add New Node. Point to Next node, Head pointing New node
    def _add(self, value):
        self.length += 1
        self.head = Node(value, self.head)

    # Find Node through Index
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    # Find node by Value
    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    # DELET NODE
    def deleteNode(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delte(prev, node)
        else:
            print(f"There's no {index} Node")

    def deleteNodeByValue(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, node)
        else:
            print(f"There's no {value} node")
