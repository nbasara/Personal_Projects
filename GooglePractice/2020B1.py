t = int(input())
for i in range(1, t+1):
	n = int(input())
	peaks  = 0
	trail = input().split(" ")
	for k in range(len(trail)):
		trail[k] = int(trail[k])
	for j in range(1, n-1):
		if trail[j-1] < trail[j] and trail[j] > trail[j+1]:
			peaks = peaks + 1
	print("Case #" + str(i) + ": " + str(peaks))