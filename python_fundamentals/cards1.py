import random

def define_cards():
    rank_string = ("ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king")
    suit_string = ("clubs","diamonds","hearts","spades")
    cards = []
    for suit in range(4):
        for rank in range(13):
            card_string = rank_string[rank] + " of " + suit_string[suit]
            cards.append(card_string)
        return cards



print define_cards()

