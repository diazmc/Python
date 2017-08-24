class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print self.suit, self.val

    def shuffle(self):
        random.shuffle(card)


suits = ['spades','hearts','diamonds','clubs']

values =['A','2','3','4','5','6','7','8','9','10','J','Q','K']

print 