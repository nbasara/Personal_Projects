import random

#global variables
#card Suits
cardSuit1 = []
cardSuit2 = []
cardSuit3 = []
cardSuit4 = []
cardSuit5 = []
#card Value
cardRank1 = []
cardRank2 = []
cardRank3 = []
cardRank4 = []
cardRank5 = []
#classification for hand
result    = []


#mainFunction
def main():
	print("Let's do this!\n")
	hands = getHands()

	hand1 = findHand(hands)
	#hand2 = findHand(hands)
	#hand3 = findHand(hands)
	#hand4 = findHand(hands)
	#hand5 = findHand(hands)

	resultHand1 = findResult(hand1)
	check = checkResult(hand1, resultHand1)

def getHands():
	file = open("poker-hand-training-true.data", "r")
	hands = 0
	for line in file:
		holder = line
		hand = holder.split(",", -1)
		cardSuit1.append(int(hand[0]))
		cardSuit2.append(int(hand[2]))
		cardSuit3.append(int(hand[4]))
		cardSuit4.append(int(hand[6]))
		cardSuit5.append(int(hand[8]))
		cardRank1.append(int(hand[1]))
		cardRank2.append(int(hand[3]))
		cardRank3.append(int(hand[5]))
		cardRank4.append(int(hand[7]))
		cardRank5.append(int(hand[9]))
		result   .append(int(hand[10]))
		hands = hands + 1
	file.close()
	return hands

def findHand(a):
	x = random.randint(0, a + 1)
	return x

def findResult(a):
	flush = checkFlush(a)
	if flush != 1:
		pairs = checkPairs(a)
	if pairs == 0:
		straight checkStraigt(a)
		if straight == 1 and flush == 1:
			return 8
		elif straight == 0 and flush == 1:
			return 5
		elif straight != 0 and flush == 0:
			return 4
		elif straight == 2 and flush == 1:
			return 9
		else:
			return 0
	else:
		if   pairs == 1:
			return 1
		elif pairs == 2:
			return 2
		elif pairs == 3:
			return 3
		elif pairs == 4:
			return 7
		else:
			return 6

def checkFlush(a):
	if cardSuit1[a] == cardSuit2[a] and cardSuit2[a] == cardSuit3[a] and cardSuit3[a] == cardSuit4[a] and cardSuit4[a] == cardSuit5[a]:
		return 1
	else:
		return 0

def checkPairs(a):
	p = 0
	if cardRank1[a] == cardRank2[a]:
		p = p + 1
	if cardRank1[a] == cardRank3[a]:
		p = p + 1
	if cardRank1[a] == cardRank4[a]:
		p = p + 1
	if cardRank1[a] == cardRank5[a]:
		p = p + 1
	if cardRank2[a] == cardRank3[a]:
		p = p + 1
	if cardRank2[a] == cardRank4[a]:
		p = p + 1
	if cardRank2[a] == cardRank5[a]:
		p = p + 1
	if cardRank3[a] == cardRank4[a]:
		p = p + 1
	if cardRank3[a] == cardRank5[a]:
		p = p + 1
	if cardRank4[a] == cardRank5[a]:
		p = p + 1

	return p

def checkResult(a, b):
	if b == result[a]:
		return 1
	else:
		return 0


main()