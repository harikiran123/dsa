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
    
    def del_from_pos(self,pos):
        if self.head is None:
            print("list is empty")
        if pos == 0:
            deleted_value=self.head.data
            self.head=self.head.next
            print(f"{deleted_value} is deleted successfully")
            return
        count =0
        current = self.head
        while current is not None and count < pos - 1 :
            current= current.next
            count += 1
        if current is None or current.next is None:
            print("pos not found")
            return 
        else:
            deleted_value=current.next.data
            current.next = current.next.next
            print(f"{deleted_value} is deleted successfully")
            return
               
            

linked_list=linkedlist()
n = int(input("enter the no.of elements need to enter"))
for i in range(n):
    data=int(input(f"enter the {i+1} element : "))
    linked_list.add_at_end(data)
linked_list.display()   

pos=int(input("enter the position to be deleted : "))
linked_list.del_from_pos(pos)
linked_list.display()