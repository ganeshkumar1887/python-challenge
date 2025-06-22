def arrSortedOrNot(arr,n):
    if (n==0 or n==1):
        return True
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            return False
    return True

arr = [20,30,40,50,60]
n = len(arr)
if(arrSortedOrNot(arr,n)):
    print("yes")
else:
    print("No")