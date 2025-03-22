class insertion_sort:
    def __init__(self):
        self.list=[]
    
    def add_elements_to_list(self,data):
        self.list.append(data)


    def sort(self):
        for i in range(len(self.list)):
            j = i

            while self.list[j - 1] > self.list[j] and j > 0:
                self.list[j-1],self.list[j] = self.list[j], self.list[j-1]
                j -= 1
    def display(self):
        return self.list

insertion_sort_obj=insertion_sort()
n = int(input("enter the no.of elements need to enter"))
for i in range (n):
    data=int(input(f"enter the {i + 1} value"))
    insertion_sort_obj.add_elements_to_list(data)
print(insertion_sort_obj.display())
insertion_sort_obj.sort()
print(insertion_sort_obj.display())
