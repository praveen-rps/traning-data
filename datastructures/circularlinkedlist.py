from node import Node

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_at_beginning(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def display(self):
        if not self.head:
            print("list is empty")
            return
        temp = self.head
        print("The Elements in circular fashion")
        while True:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break
        print("Back to Head or First")
        print(temp.data, end="->")

if __name__ == "__main__":
    clinkedlist = CircularLinkedList()
    clinkedlist.insert(1)
    clinkedlist.insert(2)
    clinkedlist.insert(3)
    clinkedlist.display()