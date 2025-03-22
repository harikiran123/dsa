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

    def add_at_beg(self,element_beg):
        
        '''
        Description: this function add the elements at the begining of the linked list
        parameters: self
        Return: noone
        '''

        new_node=Node(element_beg)
        new_node.next = self.head
        self.head = new_node
        

linked_list = LinkedList()
n = int(input("enter the no.of elements you need to enter"))
for i in range(n):
    data = input(f"enter  the {i + 1} element: ")
    linked_list.add_at_end(data)
print("original llis")
linked_list.display()

element_beg=int(input("enter the element you need to add at begining"))
linked_list.add_at_beg(element_beg)
print("updated list")
linked_list.display()