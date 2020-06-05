# War card game

# Create all the 52 Cards
# Share cards between player and computer.

from random import shuffle

print("WELCOME TO THE WAR GAME")

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
            return 1

        else:
            return int(card[1:])

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

        return [player_one_deck, player_two_deck]

class addCard():

    def __init__(self, deck, card1, card2):
        self.deck = deck
        self.card1 = card1
        self.card2 = card2
        pass

    def add_card(self):

        self.deck.extend([self.card1, self.card2])
        return self.deck

class removeCard():

    def __init__(self, deck, card):
        self.deck = deck
        self.card = card
        pass

    def remove_card(self):

        card_index = self.deck.index(self.card)
        removed_card = self.deck.pop(card_index)
        return removed_card

class gamePlay():

    def __init__(self):
        pass

    def ask(self):

        q_play = input("Do you like to play (y or n)? ")

        if q_play not in ["y", "n"]:

            gamePlay.ask(self)

        if q_play == "y":

            gamePlay.pull_card(self)

        if q_play == "n":

            print("See you later!")
            # exit()

    def cards_on_table(self):

        a = shareCards.main(self)[0]
        b = shareCards.main(self)[1]

        computer_deck = a
        player_deck = b

        return [computer_deck, player_deck]

    def pull_card(self):

        computer_deck1 = gamePlay.cards_on_table(self)[0]
        player_deck1 = gamePlay.cards_on_table(self)[1]
        shuffle(computer_deck1)
        shuffle(player_deck1)

        while computer_deck1 != [] and player_deck1 != []:

            print(f"Your deck strength: {len(player_deck1)}")

            print(f"Computer card: {computer_deck1[0]}")

            input("Enter to pull the card: ")
            
            print(f"your card: {player_deck1[0]}")

            input("Enter to continue: ")

            computer_score = allCards.card_value(self, card = computer_deck1[0])
            player_score = allCards.card_value(self, card = player_deck1[0])

            print(computer_score, player_score)

            if computer_score > player_score:

                # Remove player card from their deck
                card_player_lost = removeCard(player_deck1, player_deck1[0]).remove_card()
                # Remove the top card from computer's deck
                computer_top_card = removeCard(computer_deck1, computer_deck1[0]).remove_card()
                # Add the 2 removed cards to the computer's deck.
                addCard(computer_deck1, computer_top_card, card_player_lost).add_card()

                print("Computer Won the round.\n")

            elif computer_score < player_score:

                # Remove computer's card from its deck
                card_computer_lost = removeCard(computer_deck1, computer_deck1[0]).remove_card()
                # Remove the top card from player's deck
                player_top_card = removeCard(player_deck1, player_deck1[0]).remove_card()
                # Add the 2 removed cards to the player's deck.
                addCard(player_deck1,player_top_card, card_computer_lost).add_card()

                print("You Won the round.\n")

            elif computer_score == player_score and (len(player_deck1) < 3 or len(computer_deck1) < 3):

                break

            elif computer_score == player_score:

                    # This loot will be added to the deck of whoever wins.
                    card_loot = []

                    # Remove the top cards from computer and player deck.
                    computer_top_card = removeCard(computer_deck1, computer_deck1[0]).remove_card()
                    card_loot.append(computer_top_card)
                    player_top_card = removeCard(player_deck1, player_deck1[0]).remove_card()
                    card_loot.append(player_top_card)

                    while computer_score == player_score and len(player_deck1) >= 3 and len(computer_deck1) >= 3:

                        input("It's a draw, the two cards are kept aside.\nTo continue, three more will be pulled from both the decks.\nThe top cards will be compared\nEnter to continue...")
                        
                        player_pull_card_1 = removeCard(player_deck1, player_deck1[0]).remove_card()
                        card_loot.append(player_pull_card_1)
                        player_pull_card_2 = removeCard(player_deck1, player_deck1[0]).remove_card()
                        card_loot.append(player_pull_card_2)
                        player_pull_card_3 = removeCard(player_deck1, player_deck1[0]).remove_card()
                        card_loot.append(player_pull_card_3)

                        computer_pull_card_1 = removeCard(computer_deck1, computer_deck1[0]).remove_card()
                        card_loot.append(computer_pull_card_1)
                        computer_pull_card_2 = removeCard(computer_deck1, computer_deck1[0]).remove_card()
                        card_loot.append(computer_pull_card_2)
                        computer_pull_card_3 = removeCard(computer_deck1, computer_deck1[0]).remove_card()
                        card_loot.append(computer_pull_card_3)

                        computer_score = allCards.card_value(self, card = computer_pull_card_1)
                        player_score = allCards.card_value(self, card = player_pull_card_1)
                        continue
                    
                    print(f"Computer top card: {computer_pull_card_1}")
                    print(f"Your top card: {player_pull_card_1}")
                    input("Please enter to continue: ")

                    if player_score > computer_score:

                        player_deck1.extend(card_loot)
                        print(f"You have won the round, you deck strength is {len(player_deck1)}")
                        input("Please enter to continue: ")

                    if player_score < computer_score:

                        computer_deck1.extend(card_loot)
                        print(f"Computer has won the round, you deck strength is {len(player_deck1)}")
                        input("Please enter to continue: ")

        winDecide.main(self, computer_deck1, player_deck1)

class winDecide():

    def __init__(self):
        pass

    def main(self, computer_deck, player_deck):
        self.computer_deck = computer_deck
        self.player_deck = player_deck
        
        if len(computer_deck) > len(player_deck):
            print("The Computer has won the WAR.")

        else:
            print("You have won the WAR!")

        game1.ask()

game1 = gamePlay()
game1.ask()
