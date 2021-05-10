# This program uses a dictionary as a deck of cards.
import random
import collections
import os 
os.chdir(r"C:\Users\Nick\Desktop\CPCC\.github.io\csc 121\Chapter 9")

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Deal the cards to each player.
    deal_cards(deck)

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck

# Deal a card to each player until one player exceeds a hand value over 21
def deal_cards(deck):

    player_one_hand_value = 0
    player_two_hand_value = 0

    while True:

        if player_one_hand_value > 21 or player_two_hand_value > 21:
            break
        else:
            card = random.choice(list(deck))
            if deck[card] == 1:
                if player_one_hand_value <= 10:
                    deck[card] = 11
            player_one_hand_value += deck[card]
            print("Player 1 gets " + str(card) + ". Their current hand value is " + str(player_one_hand_value) + "\n")
            
            card = random.choice(list(deck))
            if deck[card] == 1:
                if player_two_hand_value <= 10:
                    deck[card] = 11
            player_two_hand_value += deck[card]
            print("Player 2 gets " + str(card) + ". Their current hand value is " + str(player_two_hand_value) + "\n")
    
    if player_one_hand_value <= 21:
        print("Player 1 wins!")
    elif player_two_hand_value <= 21:
        print("Player 2 wins!")
    else:
        print("Tie! No one wins!")

# Call the main function.
if __name__ == '__main__':
    main()