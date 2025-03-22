class bubble:
    def __init__(self):
        self.list=[]
    
    def add_elements_to_list(self,data):
        self.list.append(data)


    def sort(self):
        for i in range(len(self.list)-1,0,-1):
            for j in range(i):
                if self.list[j] > self.list[j+1]:
                    self.list[j],self.list[j+1]=self.list[j+1],self.list[j]        

    def display(self):
        return self.list

bubble_sort=bubble()
n = int(input("enter the no.of elements need to enter"))
for i in range (n):
    data=int(input(f"enter the {i + 1} value"))
    bubble_sort.add_elements_to_list(data)
print(bubble_sort.display())
bubble_sort.sort()
print(bubble_sort.display())
