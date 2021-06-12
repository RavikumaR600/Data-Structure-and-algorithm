class Node:
    def __init__(self,data):
        self.data= data
        self.ref= None
        self.nref= None 
        self.pref=None

class douly_LinkedList:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            n= self.head
            while n is not None:
                print(n.data ,"-->",end=" ")
                n=n.nref

    def print_ll_rev(self):
        print()
        if self.head is None:
            print("LinkedList is empty")
        else:
            n= self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data ,"-->",end=" ")
                n=n.ref

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LinkedList is not empty")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n= self.head
            while n.nref is not None:
                n= n.nref
                n.nref = new_node
                new_node.pref = n
    
    def add_after(self,data,x):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("given node is not present in the double linkedList")
            else:
                new_node = Node(data) 
                new_node.nref = n.nref
                new_node.pref = n 
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("given node is not present in the double linkedList")
            else:
                new_node = Node(data) 
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head= new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("douly_LinkedList is empty")
            return 
        if self.head.nref is None:
            self.head = None
            print("douly_LinkedList is empty so can't delete")
        else:
            self.head = self.head.n.ref 
            self.pref = None

    def delete_end(self):
        if self.head is None:
            print("douly_LinkedList is empty")
            return 
        if self.head.nref is None:
            self.head = None
            print("douly_LinkedList is empty so can't delete")
        else:
            n= self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("douly_LinkedList is empty")
            return 
        if self.head.nref is None:
            if x==self.head.data:
                self.head = None
        else:
            print("x is not present is DLL")
            return
        if self.head.data == x:
            self.head =self.head.nref
            self.head.pref = None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref =n.pref 
            n.pref.nref= n.nref
        else:
            if n.data ==x:
                n.pref.nref = None 
            else:
                print("x is not in DLL")


dll= douly_LinkedList()
#  dll.add_before(600,200)
# dll.add_begin(100)
# dll.add_begin(200)
#  dll.add_after(400,200)
#  dll.insert_empty(10)
#  dll.insert_empty(20)
# dll.print_ll_rev()
# dll.delete_begin()
# dll.delete_end()
# dll.delete_by_value(200)
# dll.print_ll()