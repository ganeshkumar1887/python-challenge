def two_sum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return True
    return False

arr = [0, -1, 2, -3, 1]
target = -2
if two_sum(arr, target):
    print("true")
else:
    print("false")