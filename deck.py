from cards import Cards 
from random import shuffle,randint


class Deck:
    
    CARDS_IN_DECK =15
   
    def __init__(self):
        self.deck = self.__create_deck()

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = cards
        
    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, deck):
        self.__deck = deck     

    # Private Methods

    def __create_deck(self): 
        deck =[ ]
        characters = ["Duke","Assassin","Ambassador",
                      "Captain","Contessa"]
        for i in range(3):
            for character in characters:
                deck.append(Cards(character))
        shuffle(deck)
        return deck
    
    def pick_card_and_remove(self):
        while True:
            random = randint(0,14)
            if self.deck[random].in_deck == True:
                self.deck[random].in_deck =  False
                return self.deck[random].influence
                break
                    

    def __str__(self): 
        str_deck = ''
        deck_elements = [ ]

        for i in range(len(self.deck)): 
            if self.deck[i].in_deck == True:
                deck_elements.append(str(self.deck[i]))

        str_deck += ' '.join(deck_elements) +'\n'

        return str_deck

    def cards_still_on_deck(self,deck):
       pass
       #for card in range(len(self.deck)):
            #for col in range(len(self.grid[0])):
                #if not self.grid[row][col].discovered:
                   # return True
        #return False
        

    def check_play(self, played_card):
        #if played_card = 
        #quiero que me chequee la funcion que elijio el player para su carta, como validar coordenadas
        pass 

    def show__played_card(self):
        self.deck.in_hand = False
        #quiero mostrarle solo al jugador sus cartas y luego su carta jugada







#def __create_grid(self):
 #       number_of_rows, number_of_cols = self.__get_rows_and_cols()
  #      cards = self.cards.copy()
   #     shuffle(cards)
    #    grid = []
     ##   for row in range(number_of_rows):
       #     grid.append([])
         #       grid[row].append(cards.pop())
        #    for col in range(number_of_cols):
       # return grid