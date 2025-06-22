def largest(arr,n):
    mx = arr[0]
    for i in range(1,n):
        if arr[i]> mx:
            mx = arr[i]
    return mx   

arr = [200,40,50,30,65]
n = len(arr)
ans = largest(arr,n)
print("largest number in array = ",ans)