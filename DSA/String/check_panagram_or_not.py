from string import ascii_lowercase
def checkPangram(s):
    for ch in ascii_lowercase:
        found = False
        
        for i in range(len(s)):
            if ch == (s[i].lower()):
                found = True
                break
        
        if found == False:
            return False
    return True

if __name__ == "__main__":
    s = "The quick brown fox jumps over the lazy dog"
    if checkPangram(s) == True:
        print("true")
    else:
        print("false")