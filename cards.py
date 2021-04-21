class Cards:

    def __init__(self,influence):
        self.__influence = influence 
        self.in_hand = False
        self.in_deck = True


    @property
    def influence(self):
        return self.__influence

    @property
    def in_deck(self):
        return self.__in_deck

    @in_deck.setter
    def in_deck(self, in_deck):
        self.__in_deck = in_deck

    @property
    def in_hand(self):
        return self.__in_hand

    @in_hand.setter
    def in_hand(self, in_hand):
        self.__in_hand = in_hand

    def __str__(self):

        return str(self.influence).center(7)

    '''def __str__(self):
        if self.in_deck:
            string = ' '
            return string.center(7)
        elif self.in_hand:
            return '[...]'
        else:
            return str(self.influence).center(7) '''