import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# Class to make an individual card (Ex. Ace of Spades)
class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# Class to make a deck consisting of cards from card class
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Cards(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# Class to create player which can hold cards
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)}'


# Converts the players hand into a list of values corresponding to card values
def convert_values(name):
    card_values = []
    for card in name.all_cards:
        card_values.append(values[card.rank])

    return card_values


# Returns the total value of players hand
def add_vals(val_list):
    player_total = 0
    for val in val_list:
        if val == 14:
            if player_total + 11 > 21:
                player_total += 1
            else:
                player_total += 11
        elif val == 11 or val == 12 or val == 13:
            player_total += 10
        else:
            player_total += val
    return player_total


# Hit and Stand Logic
def hit_stand(cardTotal):
    passThru = True
    while passThru or cardTotal < 21:
        hit_or_stand = (input("Hit or Stand?: ")).lower()
        loc = len(player1.all_cards)
        if hit_or_stand == 'hit' or hit_or_stand == 'h':
            player1.add_card(game_deck.deal_one())
            time.sleep(2)
            print(f'Hit card: {player1.all_cards[loc]}')
            time.sleep(2)
            playVal = convert_values(player1)
            cardTotal = add_vals(playVal)
            print(f"Total: {cardTotal}")
            passThru = False
        elif hit_or_stand == 'stand' or hit_or_stand == 's':
            break
        else:
            print('Invalid input, enter "hit" or "stand" ')
    return cardTotal


# Win or Lose logic for blackJack
def game_logic(playerTotal, dealerTotal):
    global third_card
    over = False
    while not over:
        if dealerTotal < 16:
            dealer.add_card((game_deck.deal_one()))
            third_card = values[dealer.all_cards[2].rank]
            time.sleep(2)
            print(f"Dealers Third Card: {dealer.all_cards[2]}")
            dealerTotal += third_card
        elif dealerTotal > 21:
            time.sleep(2)
            print(f'Dealer Total: {dealerTotal}')
            time.sleep(2)
            print("Player Wins!")
            over = True
        elif playerTotal < dealerTotal:
            print(f'Dealer Total: {dealerTotal}')
            time.sleep(2)
            print("Dealer Wins!")
            over = True
        else:
            time.sleep(2)
            print(f'Dealer Total: {dealerTotal}')
            time.sleep(2)
            print("Player Wins!")
            over = True


# Logic to start new round or quit game
def aNew_round():
    global round_on
    global game_on

    new_round = False
    while not new_round:
        again = input("Play Again? (y or n): ").lower()
        if again == 'y':
            new_round = True
        elif again == 'n':
            round_on = False
            game_on = False
            new_round = True


player_name = input("Enter your name: ")

# Main game loop
game_on = True
while game_on:

    print("\nNew Round Starting!")
    time.sleep(4)
    round_on = True
    while round_on:
        game_deck = Deck()
        game_deck.shuffle()

        player1 = Player(player_name)
        dealer = Player("Dealer")

        for i in range(2):
            player1.add_card(game_deck.deal_one())
            dealer.add_card((game_deck.deal_one()))

        player_vals = convert_values(player1)
        dealer_vals = convert_values(dealer)

        card1 = player1.all_cards[0]
        card2 = player1.all_cards[1]
        dealer1 = dealer.all_cards[0]
        dealer2 = dealer.all_cards[1]

        card_totals = add_vals(player_vals)
        dealer_totals = add_vals(dealer_vals)

        print(f'First Card: {card1}')
        time.sleep(3)
        print(f'Second Card: {card2}')
        time.sleep(2)
        print(f'Total: {card_totals}')
        time.sleep(2)
        print(f'Dealer: {dealer1}')
        time.sleep(2)

        card_totals = hit_stand(card_totals)
        if card_totals > 21:
            time.sleep(2)
            print("Bust!")
            aNew_round()
            break
        elif card_totals == 21:
            time.sleep(2)
            print("Blackjack!")
            aNew_round()
            break

        time.sleep(2)
        print(f"Dealers Second Card: {dealer2}")
        time.sleep(2)

        game_logic(card_totals, dealer_totals)
        aNew_round()

# TO-DO: Add point system through player class
#        Test aNewRound function more
#        Test game multiple times.
