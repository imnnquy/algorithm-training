myString = input()
strLength = len(myString)
midleIndex = strLength
for counter in range(0, midleIndex):
	if(myString[counter] != myString[strLength - 1 - counter]):
		print("NO")
		exit()
print("YES")