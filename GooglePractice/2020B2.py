t = int(input())
for i in range(1, t+1):
	routes, finish = [int(s) for s in input().split(" ")]
	days = [int(s) for s in input().split(" ")]
	start = finish
	for j in range(1, routes + 1):
		start = start - (start % days[routes - j])
	print("Case #" + str(i) + ": " + str(start))


	