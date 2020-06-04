# War card game

# Create all the 52 Cards
# Share cards between player and computer.

from random import shuffle

class allCards():

    number = list(range(2, 11))
    chars = ["A", "K", "Q", "J"]
    suffix = number + chars
    symbol = ["♠", "♥", "♦", "♣"]

    def __init__(self):
        pass

    def cards(self):
        
        list_cards = [s + str(char) for s in allCards.symbol for char in allCards.suffix]

        return list_cards

    def card_value(self, card):
        self.card = card

        if card[1] in "KQJ":
            return 10

        elif card[1] == "A":
            return 11

        else:
            return int(card[1])

class shareCards():

    def __init__(self):
        pass

    def main(self):

        ini = allCards()
        all_cards = ini.cards()
        shuffle(all_cards)

        player_one_deck = []
        player_two_deck = []

        i = 0
        for card in all_cards:
            if i % 2 == 0:
                player_one_deck.append(card)
            else:
                player_two_deck.append(card)
            
            i += 1

        print(player_one_deck)
        print(player_two_deck)


a = shareCards()
a.main()