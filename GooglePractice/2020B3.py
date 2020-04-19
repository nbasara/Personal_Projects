def newString(x, pos):
	count = 0
	newLength = 0
	myString = []
	for i in range(1, (len(x)-pos)):
		if x[pos+i] == '(':
			count = count + 1
		elif x[pos+i] == ')' and count != 1:
			count = count - 1
		elif x[pos+i] == ')' and count == 1:
			newLength = i - 2
			break
	for i in range(0,newLength):
		myString.append(x[pos + 2 + i])

	return myString

def changePos(x, xPos, yPos):
	if x == 'N':
		if yPos == 1:
			yPos = 1000000000
		else:
			yPos = yPos - 1
	elif x == 'S':
		if yPos == 1000000000:
			yPos = 1 
		else:
			yPos = yPos + 1
	elif x == 'W':
		if xPos == 1:
			xPos = 1000000000
		else:
			xPos = xPos - 1
	else:
		if xPos == 1000000000:
			xPos = 1 
		else:
			xPos = xPos + 1
	return xPos, yPos

def walk(x):
	myString = []
	i = 0
	while i < len(x):
		if x[i].isalpha():
			myString.append(x[i])
		elif x[i].isdigit():
			deeper = walk(newString(x, i))
			for j in range(int(x[i])):
				myString = myString + deeper
			i = i + len(deeper) + 2
		i = i + 1
	return myString
	
t = int(input())
for i in range(1, t+1):
	ans = [1, 1]
	directions = input()
	a = walk(directions)
	for j in range(len(a)):
		ans = changePos(a[j], ans[0], ans[1])
	print("Case #" + str(i) + ": " + str(ans[0]) + " " + str(ans[1]) )

