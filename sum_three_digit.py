def square_add(n):
   fd = n//100 # hundred place
   md = (n//10)%10 # medium place
   ld = n % 10 # last digit
   return fd**2 + md**2 +ld**2
num = int(input("Enter the three digit Number::"))
if 100 <= num <=999:
   result = square_add(num)
   print(f"Sum of squares of digits: {result}")
else:
   print("invalid digit please take 3 digit number::") 