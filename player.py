class Player:
    def __init__(self,name,number)  :
        self.name = name
        self.number = number
        self.hand_of_cards = []
        self.coins= 2 #cada jugador parte con 2 monedas
        self.cards_left = 2 #cada jugador parte tiene 2 cartas
        self.played_card = [ ]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, coins):
        if coins >= 0:
            self.__coins = coins
        else:
            self.__coins = 0

    @property
    def played_card(self):
        return self.__played_card

    @played_card.setter   
    def played_card(self, played_card):
        self.__played_card = played_card

    @name.setter
    def played_card(self,played_card):
        self.__played_card = played_card


    def __str__(self):
        return str(self.name).center(7)

