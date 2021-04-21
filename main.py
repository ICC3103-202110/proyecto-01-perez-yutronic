from deck import Deck
from console import Console
from player import Player


class Game:

    NUMBER_OF_PLAYERS = Console.get_int_input('* Amount of players? [3-4] *\n  ')
    NUMBER_OF_CARDS = 15
    __players = [ ]
    __actual_player =None
    __deck = None

    @classmethod
    def play(cls):

        cls.__set_players()
        cls.__set_deck()
        cls.__give_hands_to_players()
        cls.__choosen_card()
        
        if cls.__actual_player.choosen_action == 'Income':
            Console.print_str("\n *****")
        
        
        while len(cls.__players) < 1:
            '''''
            turno 1 
            jugador hace una accion
                otro jugador puede dudar esa accion
                otro jugador puede usar un contraefecto

            desenlace

            
            checkeo
            '''''
            pass
        
        pass

    @classmethod
    def __give_hands_to_players(cls):  

        for name in cls.__players:
            name.hand_of_cards.append(cls.__deck.pick_card_and_remove())
            name.hand_of_cards.append(cls.__deck.pick_card_and_remove())
            Console.print_str(str(name.hand_of_cards))

    @classmethod
    def __set_deck(cls):
        cls.__deck = Deck()
    
    @classmethod
    def __set_players(cls):
        for i in range(1, cls.NUMBER_OF_PLAYERS + 1):
            name = Console.get_str_input_with_args(
                'Write player\'s {} name: ', [i]
            )
            cls.__players.append(Player(name, i))
        cls.__actual_player = cls.__players[0]

    @classmethod   
    def __choosen_card(cls):

        Console.clear()    
        Console.print_str_with_args('\n* Turn of player {}: *\n',[cls.__actual_player.name])
           
        if cls.__actual_player.coins >= 10:#aqui hace coup
            
            cls.__actual_player.choosen_action = 'Coup'
        else:        
            actions =['Income', 'Foreign Aid']
            
            for card in cls.__actual_player.hand_of_cards:
                if card == 'Duke':
                    actions.append('Tax')
                elif card == 'Ambassador':
                    actions.append('Exchange')
                elif card == 'Captain':
                    actions.append('Steal')
                elif card == 'Assassin' and cls.__actual_player.coins >= 3 :
                    actions.append('Assasinate')       
            
            #Console.print_str(str(actions))
            Console.print_str('* Take one action: *\n ')
            Console.print_list(actions) 

            while True:
                action = Console.get_str_input(' * Select your action *\n')
                if action in actions:
                   
                    break
                else:
                    Console.print_str('* Wrong action, please choose again * \n')

            cls.__actual_player.choosen_action = str(action)
            
        


#Player
##Mostrarle las cartas
#Y que le de a elegir cual va a usar
        
if __name__ == "__main__":
    Game.play()