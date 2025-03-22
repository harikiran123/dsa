class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedlist:

    def __init__(self):
        self.head=None
    
    def add_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("none")
    
    def del_from_end(self):
        if self.head is None :
            print("list is empty")       
        if self.head.next is None:
            deleted_value=self.head.data
            self.head = None
            print(f"{deleted_value} is successfully deleted")
        current=self.head
        while current.next.next is not None:
            current = current.next
        deleted_value=current.next.data
        current.next=None
        print(f"{deleted_value} is successfully deleted from the list")
                
            

linked_list=linkedlist()
n = int(input("enter the no.of elements need to enter"))
for i in range(n):
    data=int(input(f"enter the {i+1} element : "))
    linked_list.add_at_end(data)
linked_list.display()   

linked_list.del_from_end()
linked_list.display()