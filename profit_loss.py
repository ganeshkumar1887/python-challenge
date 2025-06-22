cp = int(input("Enter the cost price::"))
sp = int(input("Enter the selling price::"))
profit = sp - cp
loss = cp - sp
if(profit > 0):
    print(f"Rs.{profit} Profit")
else:
    print(f"Rs.{loss} Loss")