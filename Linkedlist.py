
# this class to create nodes
class Node:
    # initialize the fields of node
    def __init__(self, data):
        self.data = data
        self.ref = None

# this class to link nodes 
class LinkedList:
    def __init__(self):
        self.head = None # head is none means creating a empty linked list with no nodes

    def  print_linkedlist(self):
        if self.head is None:
            print("Linked List is empty")

        else:
            n = self.head

            while n is not None:
                print(str(n.data) + str(n.ref), "----->", end=" ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)

        # check linked list is empty or not
        if self.head is None:
            self.head = new_node

        else:
            n = self.head

            while n.ref is not None:
                n = n.ref

            n.ref = new_node

    def add_after_node(self, data, x):
        n = self.head

        while n is not None:
            if x == n.data: 
                break
            n = n.ref

        if n is None:
            print("Element is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before_node(self, data, x):

        if self.head is None:
            print("Linked list is empty")
            return 
        # if data before 1st node
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        
        # for remaining node
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("Data not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            print("Linked list is not empty")

    def delete_firstnode(self):
        if self.head is None:
            print("Linked list is empty")

        else:
            self.head = self.head.ref

    def delete_lastnode(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_middle(self, x):
        if self.head is None:
            print("Linked list is empty")
            return
        
        if x == self.head.data:
            self.head = self.head.ref
            return

        n = self.head
        while n is not None:
            if n.ref.data == x:
                break
            else: 
                n = n.ref

        if n.ref is None:
            print("Data is not in List")

        else:
            n.ref = n.ref.ref    


ll1 = LinkedList()
ll1.insert_empty(15)
ll1.add_begin(25)
ll1.add_end(65)
ll1.print_linkedlist()