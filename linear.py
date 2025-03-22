def linear(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

elements=int(input("enter the no.of elements you need to enter:"))
arr=[]
for i in range(elements):
    data=int(input(f"enter the {i+1} element"))
    arr.append(data)
print(arr)
n=int(input("enter the number you want to serch: "))
pos=linear(arr,n)
if pos != -1:
    print(f"{n} found at the {pos} position")
else:
    print("not found")

