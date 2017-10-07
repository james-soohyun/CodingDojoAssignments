#Deck of cards game: 52 cards, draw from deck, shuffle the deck
#Classes: card, hand, suite, table, dealer, player

import random

# # Deck of cards
deck = [
	("heart", "A"),("heart", "2"),("heart", "3"),("heart", "4"),("heart", "5"),("heart", "6"),("heart", "7"),("heart", "8"),("heart", "9"),("heart", "10"),("heart", "J"),("heart", "Q"),("heart", "K"),("spade", "A"),("spade", "2"),("spade", "3"),("spade", "4"),("spade", "5"),("spade", "6"),("spade", "7"),("spade", "8"),("spade", "9"),("spade", "10"),("spade", "J"),("spade", "Q"),("spade", "K"),("club", "A"),("club", "2"),("club", "3"),("club", "4"),("club", "5"),("club", "6"),("club", "7"),("club", "8"),("club", "9"),("club", "10"),("club", "J"),("club", "Q"),("club", "K"),("diamond", "A"),("diamond", "2"),("diamond", "3"),("diamond", "4"),("diamond", "5"),("diamond", "6"),("diamond", "7"),("diamond", "8"),("diamond", "9"),("diamond", "10"),("diamond", "J"),("diamond", "Q"),("diamond", "K")
]



# # Deck of cards, suit and value are tuples- CREATING NEW CARDS
def createDeck():
	deck = []
	count = 0
	while count < 52:
		randSuit = random.randint(1,4)
		randValue = random.randint(1,13)
		tempCard = (randSuit, randValue)
		if tempCard not in deck:
			deck.append(tempCard)
			count+=1
	return deck

#Shuffle the deck
def shuffleDeck(deck, draw):
	for cards in range(0,draw):
		x = random.randint(0,len(deck)-1)
		temp = deck[len(deck)-1]
		deck[len(deck)-1] = deck[x]
		deck[x] = temp
		tempCard = deck.pop()


# def shuffleDeck(deck):
# 	for index in range(1,53):
# 		x = random.randomint(0,51)
# 		temp  = deck[index]
# 		deck[index]= deck[x]
# 		deck[x]=temp

#Draw a unique card
def drawHand(draw):
	hand = []
	for count in range(0, draw):
		myCard = newDeck.pop()
		hand.append(myCard)
	return hand

#Drawing from deck

class Deck():
	def __init__(self):
		self.deck = deck









