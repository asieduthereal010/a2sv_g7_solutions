n, k = [int(i) for i in input().split(" ")]
arr = [int(i) for i in input().split(" ")]
arr.sort() # have to do this for 'general cases'

if k == 0: 
    if arr[0] == 1: 
        print(-1)
    else: 
        print(1)
elif k == n: 
    if n == 1: 
        if arr[0] == 1: 
            print(-1)
        else: 
            print(arr[n-1])
    else: 
        print(arr[n-1])
else:
    if arr[k-1] == arr[k]: 
        print(-1)
    else: 
        print(arr[k-1] + ((arr[k]-arr[k-1])-1)) 
