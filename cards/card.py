'''
its a card class where this class holds a card value for each card , suit of card of which it should belong 
      SUIT,RANK,VALUE
'''

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
      'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
      def __init__(self,suit,rank):
            # suit and rank are called as Attributes
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

      def __str__(self):
            return self.rank + " of " + self.suit

two_hearts = Card('Hearts','Two')
print(two_hearts)

'''
Deck class returns a card class object not a normal python data type 
'''

class Deck:
      def __init__(self):
            #creating a list for all cards 
            self.all_cards = []
            
            for suit in suits:
                  for rank in ranks:
                        # creating a card object 
                        
                        create_newCard = Card(suit,rank)
                        self.all_cards.append(create_newCard)  # appending the newly created card to empty list of all cards 

new_deck = Deck()
print(new_deck.all_cards[-1])