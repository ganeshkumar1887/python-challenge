def linear_search(arr,tar):
    for i in range(len(arr)):
        if arr[i] == tar:
            return i
    return -1

arr = [2,4,5,6,7,8,11,23]
tar = 8
result = linear_search(arr,tar)
if result != -1:
    print(f"Element is found at index {result}")
else:
    print("element is not found::")