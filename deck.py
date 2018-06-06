# This is the Deck Object to be used by the BlackJack or other files
# Wahab Ehsan

import card


class DeckOfCards:
    cards = []

    def __init__(self):
        self.addCards()

    def addCards(self):
        for x in range(2, 15):
            self.cards.append(card.Card("Hearts", x))
            self.cards.append(card.Card("Clubs", x))
            self.cards.append(card.Card("Spades", x))
            self.cards.append(card.Card("Diamonds", x))

    def toString(self):

        content = "["
        for x in self.cards:
            content += x.toString() + ", "
        # Returns the content and removes the extra space and comma by a backspace times two.
        return content + "\b"*2 + "]"

