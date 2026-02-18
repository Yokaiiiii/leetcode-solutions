# creating a class to create a linked list


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # this will link this node with the next node down the linked list line

    # now if i wanna add anything to a linked list
    # then i gotta do few stuffs
    # 1) link the previous node with this new node
    # 2) add the value which you wanna store in this new node
    # 3) Link this new node to a none (which can later be replace with another node when appending again)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(val)

    def iterate(self):
        if not self.head:
            return -1
        curr = self.head
        while curr.next:
            print(curr.val)
            curr = curr.next
        print(curr.val)


l1 = LinkedList()

l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)

l1.iterate()
