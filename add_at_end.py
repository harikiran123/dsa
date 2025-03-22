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

linked_list = LinkedList()
linked_list.add_at_end(10)
linked_list.add_at_end(20)
linked_list.add_at_end(30)
linked_list.display()
