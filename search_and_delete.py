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
    
    def search_and_delete(self,del_num):
        if self.head is None:
            print("list is empty")

        if self.head.data == del_num:
            self.head = self.head.next
            print(f"{del_num} is deleted successfully from the list")  
            return 
        current = self.head
        while current.next is not None:
            if current.next.data == del_num:
                current.next = current.next.next
                print(f"{del_num} is deleted successfully form the list")
                return
            current = current.next
        
        print("not found")
            

linked_list=linkedlist()
n = int(input("enter the no.of elements need to enter"))
for i in range(n):
    data=int(input(f"enter the {i+1} element : "))
    linked_list.add_at_end(data)
linked_list.display()   

del_num=int(input("enter the number you want to search and delete"))
linked_list.search_and_delete(del_num)
linked_list.display()