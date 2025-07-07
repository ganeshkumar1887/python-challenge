def isbinary(s):
    for i in range(len(s)):
        if s[i] != "0" and s[i] !="1":
            return False
        return True
s="10111010"
print("true" if isbinary(s) else "false")