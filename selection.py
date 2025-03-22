class bubble:
    def __init__(self):
        self.list=[]
    
    def add_elements_to_list(self,data):
        self.list.append(data)


    def sort(self):
        for i in range(len(self.list)) :
            minpos=i
            for j in range (i,len(self.list)) :
                if self.list[j] < self.list[minpos]:
                    minpos = j
            self.list[i],self.list[minpos]=self.list[minpos],self.list[i]
            
                


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
