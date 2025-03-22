from collections import deque

class queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,data):
        self.queue.append(data)
        print(f"{data} is added to queue") 
    
    def dequeue(self):
        if not self.queue:
            print("list is empty")
            return 
        else:
            removed_element=self.queue.popleft()
            print(f"dequeded {removed_element}")
    
    def display(self):
        print("current list: ",list(self.queue))


queue_operation = queue()
while True:
    print("select 1 to do enqueue opetation ")
    print("select 2 to do dequeue opetation ")
    print("select 3 to display the queue")
    print("select 4 from to exit frmo the program")
    select = int(input("select one number to do opetation :"))

    if select == 1:
        data=int(input("enter the element you need to enter "))
        queue_operation.enqueue(data)
    
    elif select == 2:
        queue_operation.dequeue()
    
    elif select == 3:
        queue_operation.display()
    
    elif select == 4:
        print("exitint from the program ")
        break
    
    else:
        print("select only 1 to 4 only")



