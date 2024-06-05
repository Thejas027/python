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

# two_hearts = Card('Hearts','Two')
# print(two_hearts)

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
                        
      def shuffle(self):
            random.shuffle(self.all_cards)
            
      def deal_one(self):
            return self.all_cards.pop()
      


# new_deck = Deck()
# print(new_deck.all_cards[-1])

# new_deck.shuffle()
# print(new_deck.all_cards[-1])

# mycard = new_deck.deal_one()
# print(mycard)

############ Players class 
'''
      used to hold a current list of cards of a player
            --> player can add or remove the card from the deck 
            --> player can add single or multiple card to the list 
            --> this should be visualize about translating a deck/hand of cards from top or bottom 
                  --> player 'plays' a card from the top -- pop(0)
                  --> player 'adds' a card to bottom -- append('card_name')
                        --> need to add a list of cards, then use -- extend('new_list_name')
                        
'''


class Player():
      def __init__(self,name):
            self.name = name
            self.all_cards = []   # a new attribute can be created like this
            
      def remove_one(self):
            return self.all_cards.pop(0)
            
      def add_cards(self,new_card):
            if type(new_card) == type([]):
                  # If its a list then this gets executed
                  self.all_cards.extend(new_card)
            else:
                  # If its a single card then this gets executed 
                  self.all_cards.append(new_card)
      
      def __str__(self):
            return f'Player {self.name} has {len(self.all_cards)} cards.'
            
# new_player = player('Thejas')
# print(new_player)

# new_player.add_cards(mycard)
# print(new_player)

# new_player.add_cards([mycard,mycard,mycard])
# print(new_player)


''''
      Game logic
'''

#Game setup 

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
      player_one.add_cards(new_deck.deal_one())
      player_two.add_cards(new_deck.deal_one())


game_on = True

### while game_on  ---> main section actual game logic starts here 
round_num = 0

while game_on:
      
      round_num += 1
      print(f"Round {round_num}")
      
      # This if statement checks for win of player-1
      if len(player_one.all_cards) == 0:
            print('Player one, out of cards ! Player 2 WINS!')
            game_on = False
            break
      
      # This if statement checks for win of player-2
      if len(player_two.all_cards) == 0:
            print('Player two, out of cards ! Player 1 WINS!')
            game_on = False
            break

      ## START A NEW ROUND 
      player_one_cards = []
      player_one_cards.append(player_one.remove_one())
      
      player_two_cards = []
      player_two_cards.append(player_two.remove_one())

      # while at_war --> if both the players removes the same values of cards 
      
      '''
            This loop runs when player one and player two removes the same card and both have the same value then their will be 3 cases 
                  --> player one card == player two card 
                  --> player one card > player two card 
                  --> player one card < player two card 
                  
                  
      -----> The rule used here is,
            --> If there is a tie each player needs to draw a additional of 5 cards 
            --> A player looses if they dont have at least 5 cards to play the war 
                  --> this logic can be edited as 
      '''