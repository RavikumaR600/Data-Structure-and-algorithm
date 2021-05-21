class Node:
    def __init__(self,data):
        self.data= data
        self.ref= None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n= self.head
            while n is not None:
                print(n.data ,"-->",end=" ")
                n=n.ref

    def add_beginning(self,data):
        new_node= Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete_start(self):
        if self.head is None:
            print("Linkedlist is empty ")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("LinkedList is empty")
            
        elif self.head.ref is None:
            self.head = None
        else:
            n= self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref = None

    def del_by_value(self,x):
        if self.head is None:
            print("Can't delete ,Linkedlist is empty")
            return
        if x==self.head.data:
            self.head= self.head.ref
            return
        n= self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not Present")
        else:
            n.ref= n.ref.ref

ll1=LinkedList()
ll1.add_beginning(10)
ll1.add_beginning(20)
ll1.add_beginning(40)
ll1.delete_start()
# ll1.delete_end()
# ll1.del_by_value(40)
ll1.print_ll()

