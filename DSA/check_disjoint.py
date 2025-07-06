def areDisjoint(a,b):
    for i in range(len(a)):
        for j in range(len(b)):
            
            # If any common element is found
            # given arrays are not disjoint
            if a[i] == b[j]:
                return False
    return True
a = [12, 34, 11, 9, 3]
b = [7, 2, 1, 5]

if areDisjoint(a, b):
    print("True")
else:
    print("False")