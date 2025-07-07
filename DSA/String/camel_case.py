def convertToCamelCase(s):
    res = []
    capitalizeNext = False
    for i in range(len(s)):
        if s[i] == ' ':
            capitalizeNext=True
        elif capitalizeNext:
            res.append(s[i].upper())
            capitalizeNext = False
        else:
            res.append(s[i])

    return ''.join(res)
if __name__ == "__main__":
	s = "i got intern at geeksforgeeks"
	print(convertToCamelCase(s))