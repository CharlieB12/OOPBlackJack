import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


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


game_on = True

while game_on:

    game_deck = Deck()
    game_deck.shuffle()

    player_name = input("Enter your name: ")

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
    card_totals = add_vals(player_vals)

    print(f'First Card: {card1}')
    time.sleep(3)
    print(f'Second Card: {card2}')
    time.sleep(2)
    print(f'Total: {card_totals}')
    time.sleep(2)
    print(f"Dealer: \n{dealer1}")
    time.sleep(2)

    card_totals = hit_stand(card_totals)
# TO-DO:
# 1: read up on blackjack rules
# 2: work on logic to parse the values list (bust, hit, stand, etc.)
