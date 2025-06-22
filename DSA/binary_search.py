def binary(arr,tar,low,high):
    if low<=high:
        mid = (low+high)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]<tar:
            return binary(arr,tar,mid+1,high)
        else:
            return binary(arr,tar,low,mid-1)
    return -1

arr = [2,4,5,6,7,8,11,23]
tar = 8
result = binary(sorted(arr),tar,0,len(arr)-1)
if result != -1:
    print(f"Element is found at index {result}")
else:
    print("element is not found::")