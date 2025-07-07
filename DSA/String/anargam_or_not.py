def areAnagrams(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    # Sort both strings
    s1 = sorted(s1)
    s2 = sorted(s2)

    # Compare sorted strings
    return s1 == s2

if __name__ == "__main__":
    
    s1 = "geeks"
    s2 = "kseeg"
    
    if(areAnagrams(s1,s2)):
        print("yes it is anargam")
    else:
        print("no it is not anargam")