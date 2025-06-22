v = [[5,4,7], [1,3,8], [2,9,6]]
n = len(v)
x = []
for i in range(n):
    for j in range(n):
        x.append(v[i][j])
x.sort()
k = 0
for i in range(n):
    for j in range(n):
        v[i][j] = x[k]
        k += 1
print("Sorted Matrix will be: ")
for i in range(n):
    for j in range(n):
        print(v[i][j], end=" ")
    print("")
