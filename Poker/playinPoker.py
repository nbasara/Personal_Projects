
firstAtt = []

def main():
	print("Let's do this!\n")
	openFile()
	print("Success")

def openFile():
	r = input("What file are we opening: ")
	file = open(r, "r")
	next(file)
	i = 0
	for line in file:
		holder1 = line
		holder2 = holder1.split()
		firstAtt.append(holder2[0])
	i = 0
	for j in firstAtt:
		print(firstAtt[i])
		i = i + 1
	#print(file.read())
	file.close

main()