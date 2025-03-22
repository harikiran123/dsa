def sort(arr):
        if len(arr) > 1 :            
            left_list=arr[:len(arr)//2]
            right_list=arr[len(arr)//2:]
            sort(left_list)
            sort(right_list)           
            i=0
            j=0
            k=0
            while i<len(left_list) and j < len(right_list):
                if left_list[i]<right_list[j]:
                    arr[k]=left_list[i]
                    i += 1
                else:
                    arr[k]=right_list[j]
                    j += 1
                k += 1
            while i < len(left_list):
                arr[k]=left_list[i]
                i+=1
                k+=1
            while j < len(right_list):
                arr[k]=right_list[j]
                j+=1
                k+=1

arr = [5,4,6,3,6]
sort(arr)
print(arr)