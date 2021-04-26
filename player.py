class Player:
    def __init__(self,name,number)  :
        self.name = name
        self.number = number
        self.hand_of_cards = []
        self.coins= 2 #Each player starts with two coins
        self.cards_left = 2 #Each player starts with two cards
        self.choosen_action = ''
        

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

    def __str__(self):
        return str(self.name).center(7)

