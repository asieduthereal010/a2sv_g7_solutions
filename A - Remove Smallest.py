for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    
    greater_than_1 = False
    for i in range(len(arr)-1):
        if abs(arr[i+1]-arr[i]) > 1:
           greater_than_1 = True
           break

    if greater_than_1: 
        print("NO")
    else: 
        print("YES")
