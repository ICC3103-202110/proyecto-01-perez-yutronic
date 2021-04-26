class Cards:

    def __init__(self,influence):
        self.__influence = influence 
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

    def __str__(self):

        return str(self.influence).center(7)

    