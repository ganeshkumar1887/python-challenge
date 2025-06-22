def sortRows(mat):
    for row in mat:
        row.sort()
mat = [
    [77, 11, 22, 3],
    [11, 89, 1, 12],
    [32, 11, 56, 7],
    [11, 22, 44, 33]
]
sortRows(mat)
print('[\n', end='')
for row in mat:
    print('  [', end='')
    print(', '.join(map(str, row)), end='')
    print(']')
print(']')