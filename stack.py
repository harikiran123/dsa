class stack:
    def __init__(self):
        self.stack=[]

    def push_into_stack(self,data):
        self.stack.append(data)
        print(f"{data} is added successfully")
    
    def pop_form_stack(self):
        if not self.stack:
            print("stack is empty")
            return
        else:
            poped_data=self.stack.pop()
            print(f"the elemetn {poped_data} ")
    
    def display(self):
        print("current list : " ,self.stack)

stack_obj=stack()
while True:
    print("select 1 to push to stack")
    print("select 2 to pop form stack")
    print("select 3 to dispaly ")
    print("select 4 to exit form the program ")
    select=int(input("enter the number you need to do the operation"))
    if select==1:
        data=int(input("ente the data to be inset: "))
        stack_obj.push_into_stack(data)
    elif select == 2:
        stack_obj.pop_form_stack()
    elif select == 3:
        stack_obj.display()
    elif select==4:
        print("eziting form the program...")
        break
    else:
        print("enter the number from 1 to 4 only")

