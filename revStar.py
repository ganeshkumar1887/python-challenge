n = int(input("Number of raw::"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()