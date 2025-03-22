class merge:
    def __init__(self):
        self.list=[]
    
    def add_elements_to_list(self,data):
        self.list.append(data)


    def sort(self,arr):
        
        data=arr
        
        if len(data) > 1 :
            left_list=data[:len(data)//2]
            right_list=data[len(data)//2:]
            self.sort(left_list)
            self.sort(right_list)           
            i=0
            j=0
            k=0
            while i<len(left_list) and j < len(right_list):
                if left_list[i]<right_list[j]:
                    data[k]=left_list[i]
                    i += 1
                else:
                    data[k]=right_list[j]
                    j += 1
                k += 1
            while i < len(left_list):
                data[k]=left_list[i]
                i+=1
                k+=1
            while j < len(right_list):
                data[k]=right_list[j]
                j+=1
                k+=1
    
    def display(self):
        print(self.list)
                

merge_sort=merge()
n = int(input("enter the no.of elements need to enter"))
def lis():
    for i in range (n):
        data=int(input(f"enter the {i + 1} value"))
        merge_sort.add_elements_to_list(data)
arr=lis()
merge_sort.sort(arr)
print(arr)
merge_sort.display()


