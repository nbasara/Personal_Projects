
t = int(input())  # read a line for number of cases
for i in range(1, t + 1): #I hate how this looks on VIM
  houses = []
  n, m = [int(s) for s in input().split(" ")]  # n number of houses, budget
  houses = input().split(" ")
  houses.sort()
  total = 0
  count = 0
  while(total < m):
    total = total + int(houses[count])
    if (total <= m):
      count += 1
  print("Case #{}: {}".format(i, count), flush = True)
