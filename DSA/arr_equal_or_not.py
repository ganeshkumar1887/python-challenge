def checkEqual(a,b):
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)
a = [3, 5, 2, 5, 2]
b = [2, 3, 5, 5, 2]
if checkEqual(a, b):
        print("true")
else:
        print("false")