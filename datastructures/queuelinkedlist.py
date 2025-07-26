from node import Node

class Queue:
    def __init__(self):
       self.front = None
       self.rear = None

    def is_empty(self):
        return self.front is None

    def insert(self, data):
        newNode = Node(data)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        print("Data Inserted in Queue")

    def remove(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        if self.is_empty():
            print("Queue is Empty")
        print("Elements in Queue are : ")
        temp = self.front
        while temp :
            print(temp.data, "-->")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(10)
    q.insert(20)

    q.display()

    q.remove()
    q.remove()
    q.remove()

    q.display()
    q.remove()
    q.remove()
    q.display()
