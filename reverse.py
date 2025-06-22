num = int(input("Enter a number::"))
print("Before reverse ::",num)
rev_num = 0
while num>0:
    ld = num % 10
    rev_num = rev_num *10+ld
    num = num//10
print("After reverse ::",rev_num)
