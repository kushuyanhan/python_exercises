class Node:
    def __init__(self,cargo=None,next=None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
        return str(self.cargo)

node = Node('test')
print node

node1 = Node(1)
print node1
node2 = Node(2)
print node2
node3 = Node(3)
print node3

node1.next = node2
node2.next = node3
node3.next = None

print node1.next
print '------'

def printBackward(list):
    if list == None:
        return
    head = list
    tail = list.next
    printBackward(tail)
    print head,

printBackward(node1)