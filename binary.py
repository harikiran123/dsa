pos = 0
def binary(arr,n):
    l =0
    u =len(arr) -1
    while l <= u:
        mid = (l + u)//2
        if arr[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if arr[mid] < n:
                l = mid
            else:
                u = mid

elements = int(input("enter the no.of element:"))
arr =[]
for i in range(elements):
    data = int(input(f"enter the {i+1} element"))
    arr.append(data)
print(arr)
n = int(input("enter the elements you need  to search"))

if binary(arr,n):
    print(f"{n} found in ",pos)
else:
    print("not found")

        
