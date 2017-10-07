import random

class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
	def printCard(self):
		print self.value, self.suit

class Deck(object):
	def __init__(self):
		self.cards = self.createDeck()

	def createDeck(self):
		suits = ["heart","spade","diamond","club"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		returnList = []
		for suit in suits:
			for value in values:
				returnList.append(Card(suit,value))
		return returnList

	def drawCard(self):
		return self.cards.pop()

	def shuffle(self):
		random.shuffle(self.cards)
		return self


newDeck = Deck()
newDeck.shuffle()
newDeck.cards[51].printCard()
newDeck.drawCard().printCard()
	# def shuffle(self):