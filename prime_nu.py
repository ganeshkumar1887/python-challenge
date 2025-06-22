def prime_num(n):
    if n <=1:
        return False
    for i in range(1,n):
        if n%i==0:
            return False
    return True

limit = int(input("Enter a number of limit::"))
num = 1
while num <= limit:
    if prime_num(num):
        print(num)
    num = num+1

