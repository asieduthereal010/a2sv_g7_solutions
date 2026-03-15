n,m = (int(x) for x in input().split(" "))
arr1 = [int(x) for x in input().split(" ")]
arr2 = [int(x) for x in input().split(" ")]
arr1ptr, arr2ptr = 0,0

ans = []

while arr1ptr < len(arr1) and arr2ptr < len(arr2):
    if arr1[arr1ptr] <= arr2[arr2ptr]:
        ans.append(arr1[arr1ptr])
        arr1ptr += 1
    else: 
       ans.append(arr2[arr2ptr])
       arr2[arr2ptr]
       arr2ptr += 1

if arr1ptr == len(arr1): 
    ans += arr2[arr2ptr:]
elif arr2ptr == len(arr2):
    ans += arr1[arr1ptr:]

print(" ".join([str(x) for x in ans]))
