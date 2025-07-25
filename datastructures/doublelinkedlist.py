from DNode import Dnode


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Dnode(data)
        new_node.next = self.head

        if self.head is None:
            self.head = new_node

    def insert_at_end(self,data):
        new_node = Dnode(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        print("List in Forward Direction\n")
        while temp is not None:
            print(temp.data, end="<->")
            #last = temp
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if temp is None:
            print("list is empty")
        while temp.next is not None :
            temp = temp.next

        print("List in Backward Direction\n")
        while temp:
            print(temp.data, end="<->")
            temp = temp.prev
        print("None")


if __name__ == "__main__":
    dlist = DoubleLinkedList()
    dlist.insert_at_beginning("Python")
    dlist.insert_at_end("Java")
    dlist.insert_at_end("DevOps")
    dlist.insert_at_end("Dotnet")
    dlist.display_forward()
    dlist.display_backward()