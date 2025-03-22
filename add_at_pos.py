class Node:

    '''
    Description : this class creates a blue print of the node
    '''

    def __init__(self, data):

        '''
        Description: this function creat a structure of the class
        Parameters: self,data
        Return: None
        '''
        
        self.data = data
        self.next = None

class LinkedList:

    '''
    Description: this class do the single linked list operations 
    '''

    def __init__(self):

        '''
        Description: this function creat an head 
        Parameters: self
        Return: None
        '''

        self.head = None

    def add_at_end(self, data):

        '''
        Description: this function add the new elementa at the end of the list
        Parameters: self,data
        Return: None 
        '''

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):

        '''
        Description: this function display the list from the begining to the end 
        parameters: self
        Return: noone
        '''
        
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("noen")
    
    def at_a_postion(self,element,pos_element):
        if pos_element == 0:
            new_node=Node(element)
            new_node.next=self.head
            self.head=new_node
            return 
        new_node=Node(element)
        current=self.head
        count =0
        while current is not None and count < pos_element -1 :
            current = current.next
            count += 1
        if current is None :
            print("out of the position ")
        else:
            new_node.next=current.next
            current.next = new_node

linked_list = LinkedList()
n = int(input("enter the no.of elements in the list"))
for i in range(n):
    data = int(input(f"enter the{i+1} element:"))
    linked_list.add_at_end(data)
linked_list.display()

element=int(input("enter the element to insert in specific postion:"))
pos_element=int(input("enter the element at the postion of an element: "))
linked_list.at_a_postion(element,pos_element)
linked_list.display()