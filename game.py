from deck import Deck
from console import Console
from player import Player

class Game:
    Console.print_str('  ***   COUP   ***  \n\n\n')
    while True:
        NUMBER_OF_PLAYERS = Console.get_str_input(
        'Amount of players? (3-4): ')
        if NUMBER_OF_PLAYERS == '3' or NUMBER_OF_PLAYERS == '4':
            NUMBER_OF_PLAYERS = int(NUMBER_OF_PLAYERS)
            break
        else:
            Console.print_str('* Try again, it must be 3-4 players * \n')    

    NUMBER_OF_CARDS = 15
    __players = []
    __actual_player = None
    __deck = None
    __Table = []

    ### Main Funtion
    @classmethod 
    def play(cls):

        cls.__set_players()
        cls.__set_deck()
        cls.__give_hands_to_players()

        while len(cls.__players) > 1:
            cls.__choose_the_action()                                         
            challenge = cls.__ask_players_to_challenge()                    
            if challenge[0] == True:
                cls.__challenge(cls.__actual_player,
                                cls.__players[challenge[1]])

            cls.__execute_action()
            
            Console.show_table(cls.__Table)

            cls.__clean_choseen_actions()
            cls.__check_actual_player()

        Console.show_winner(cls.__palyers[0])

    ### Setting Funtions
    @classmethod
    def __give_hands_to_players(cls):
        for name in cls.__players:
            name.hand_of_cards.append(cls.__deck.pick_card_and_remove())
            name.hand_of_cards.append(cls.__deck.pick_card_and_remove())

    @classmethod
    def __set_deck(cls):
        cls.__deck = Deck()

    @classmethod
    def __set_players(cls):
        for i in range(1, cls.NUMBER_OF_PLAYERS + 1):
            name = Console.get_str_input_with_args(
                '\nWrite player\'s {} name: ', [i])
            cls.__players.append(Player(name, i))
        cls.__actual_player = cls.__players[0]
        Console.clear()

    ### Playable Funtions
    @classmethod
    def __choose_the_action(cls):

        Console.print_str_with_args(
            '* TURN OF PLAYER {} *\n\n\n* Your influences are: *\n     ',
            [cls.__actual_player.name])
        Console.print_list(cls.__actual_player.hand_of_cards)     
 
        all_actions = ['Income', 'Foreign Aid', 'Tax', 'Exchange', 'Steal']

        if cls.__actual_player.coins >= 10: 
            cls.__actual_player.choosen_action = 'Coup'

        else:
            if cls.__actual_player.coins >= 7: 
                all_actions.append('Coup')

            if cls.__actual_player.coins >= 3:
                all_actions.append('Assassinate')

            Console.print_str('\n* Take one action: * \n ')
            Console.print_list(all_actions)  

            while True:
                action = Console.get_str_input('\n* Select your action *\n')
                if action in all_actions:

                    break
                else:
                    Console.print_str(
                        '* Wrong action, please choose again * \n')

            Console.print_str_with_args('\n* {} took the action: {} *\n',
                                        [cls.__actual_player.name, action])

            cls.__actual_player.choosen_action = action

        Console.clear()

    @classmethod
    def __ask_players_to_challenge(cls):

        challenge = [False,0]  

        if cls.__actual_player.choosen_action in [
                'Tax', 'Exchange', 'Steal', 'Assassinate'
        ]:
            Console.print_str('    * CHALLENGING PHASE * ')
            for i in range(len(cls.__players)):

                if cls.__players[i] != cls.__actual_player and challenge[
                        0] == False:

                    while True:
                        answer = Console.get_str_input_with_args(
                            '\n* {}, you wanna challenge player {}  * [ Yes / No ] \n',
                            [cls.__players[i].name, cls.__actual_player.name])

                        if answer == 'Yes' or answer == 'No':
                            if answer == 'Yes':
                                challenge[0] = True
                                challenge[1] = i
                            break
                        else:
                            Console.print_str(
        
                                '\n * You answer isn´t valid * \n')
        Console.clear()                       
        return challenge
        
    @classmethod
    def __ask_actual_player_to_challenge(cls):

        Console.print_str('    * CHALLENGING PHASE * \n ')
        challenge = False
        while True:
            answer = Console.get_str_input_with_args(
                '\n* {}, want you to challenge?* [ Yes / No ] \n',
                [cls.__actual_player.name])

            if answer == 'Yes' or answer == 'No':
                if answer == 'Yes':
                    challenge = True

                break
            else:
                Console.print_str('\n * You answer isn´t valid * \n')
        return challenge
        Console.clear()

    @classmethod
    def __challenge(cls, player_challenged,challenger):  

        possible_actions = ['Income', 'Foreign Aid']
        for card in player_challenged.hand_of_cards:
            if card == 'Duke':
                possible_actions.append('Tax')
                possible_actions.append('Block-Foreign Aid')
            elif card == 'Ambassador':
                possible_actions.append('Exchange')
                possible_actions.append('Block-Stealing')
            elif card == 'Captain':
                possible_actions.append('Steal')
                possible_actions.append('Block-Stealing')
            elif card == 'Assassin' and player_challenged.coins >= 3:
                possible_actions.append('Assasinate')
            elif card == 'Contessa':
                possible_actions.append('Block-Assassination')

        if player_challenged.choosen_action in possible_actions:  

            if player_challenged.choosen_action == 'Tax':
                cls.__deck.return_to_deck('Duke')
            elif player_challenged.choosen_action == 'Exchange':
                cls.__deck.return_to_deck('Ambassador')
            elif player_challenged.choosen_action == 'Steal':
                cls.__deck.return_to_deck('Captain')
            elif player_challenged.choosen_action == 'Assassinate':
                cls.__deck.return_to_deck('Assassin')
            elif player_challenged.choosen_action == 'Block-Assasinate':
                cls.__deck.return_to_deck('Contessa')

            player_challenged.hand_of_cards.append(
                cls.__deck.pick_card_and_remove())

            Console.print_str_with_args(
                '\n* {} loosed the challenge. {} can use {} *\n', [
                    challenger, player_challenged,
                    player_challenged.choosen_action
                ])

            challenger_cards = []
            for card in challenger.hand_of_cards:
                challenger_cards.append(card)

            Console.print_list(challenger_cards)
            if len(challenger_cards) == 2:
                while True:
                    discard = Console.get_str_input_with_args(
                        ' * {}:Select the card that do you want to discard *\n',[challenger.name])
                    if discard in challenger_cards:
                        break
                    else:
                        Console.print_str(
                            '* Wrong selection, please choose again * \n')
            else:
                discard = challenger_cards[0]

            
            challenger.hand_of_cards.remove(discard)
            cls.__Table.append(discard)
            Console.print_str_with_args('* {}, your cards left are: *',[challenger.name])
            Console.print_list(challenger.hand_of_cards)

        else:

            Console.print_str_with_args(
                '\n* {} loosed the challenge. He can´t use {} *\n',
                [player_challenged, player_challenged.choosen_action])

            challenged_cards = []
            for card in player_challenged.hand_of_cards:
                challenged_cards.append(card)

            Console.print_list(challenged_cards)

            if len(challenged_cards) == 2:
                while True:
                    discard = Console.get_str_input_with_args(
                        '* {} : Select the card that do you want to discard *\n\n',
                        [player_challenged])
                    if discard in challenged_cards:
                        break
                    else:
                        Console.print_str(
                            '* Wrong selection, please choose again * \n')
            else:
                discard = challenged_cards[0]

            cls.__Table.append(discard)
            player_challenged.hand_of_cards.remove(discard)

            Console.print_str_with_args('\n* {}, your cards left are: *\n',[player_challenged.name])
            Console.print_list(player_challenged.hand_of_cards)
            player_challenged.choosen_action = ''

        Console.clear()

    @classmethod
    def __execute_action(cls): 
        if cls.__actual_player.choosen_action != '':
            Console.print_str_with_args('    *{} Effect* \n ',
                [cls.__actual_player.choosen_action])

            if cls.__actual_player.choosen_action == 'Income':  # INCOME
                cls.__Income(cls.__actual_player)
                Console.print_str_with_args(
                    '\n*{} has {} coins now *\n',
                    [cls.__actual_player, cls.__actual_player.coins])

            elif cls.__actual_player.choosen_action == 'Foreign Aid':  # FOREIGN AID
                counter = cls.__counter_action()
                if counter[0] == True:
                    Console.print_str_with_args(
                        '\n*{} counter-atack with {} *\n', [
                            cls.__players[counter[1]],
                            cls.__players[counter[1]].choosen_action
                        ])

                    challenge = cls.__ask_actual_player_to_challenge()
                    if challenge == True:
                        cls.__challenge(cls.__players[counter[1]],
                                        cls.__actual_player)
                    else:
                        cls.__Foreign_aid(cls.__actual_player)
                        Console.print_str_with_args(
                            '\n*{} has {} coins now *\n',
                            [cls.__actual_player, cls.__actual_player.coins])
                else:
                    cls.__Foreign_aid(cls.__actual_player)
                    Console.print_str_with_args(
                        '\n*{} has {} coins now *\n',
                        [cls.__actual_player, cls.__actual_player.coins])

            elif cls.__actual_player.choosen_action == 'Coup':  ### COUP
                Target_number = cls.__choosen_player_to_attack()
                cls.__Coup(cls.__actual_player, cls.__players[Target_number], cls.__deck)
                Console.print_str_with_args(
                    '\n*{} made a Coup, he has {} coins now *\n',
                    [cls.__actual_player.name, cls.__actual_player.coins])

            elif cls.__actual_player.choosen_action == 'Tax':  ### TAX
                cls.__Duke_act(cls.__actual_player)
                Console.print_str_with_args(
                    '\n*{} has {} coins now *\n',
                    [cls.__actual_player, cls.__actual_player.coins])

            elif cls.__actual_player.choosen_action == 'Assassinate':  ### ASSASSINATE
                Target_number = cls.__choosen_player_to_attack()
                counter = cls.__counter_action()
                if counter[0] == True:
                    Console.print_str_with_args(
                        '\n*{} counter-atack with {} *\n', [
                            cls.__players[counter[1]],
                            cls.__players[counter[1]].choosen_action
                        ])

                    challenge = cls.__ask_actual_player_to_challenge()
                    if challenge == True:
                        cls.__challenge(cls.__players[counter[1]],
                                        cls.__actual_player)
                    else:
                        cls.__Assassin_act(cls.__actual_player,
                                        cls.__players[Target_number], cls.__deck)
                        Console.print_str_with_args(
                            '\n*{} has murder a influence of  {} *\n',
                            [cls.__actual_player, cls.__players[Target_number]])
                else:
                    cls.__Assassin_act(cls.__actual_player,
                                    cls.__players[Target_number], cls.__deck)
                    Console.print_str_with_args(
                        '\n*{} has murder a influence of  {} *\n',
                        [cls.__actual_player, cls.__players[Target_number]])

            elif cls.__actual_player.choosen_action == 'Exchange':  ### EXCHANGE
                cls.__Ambassador_act(cls.__actual_player, cls.__deck)
                Console.print_str_with_args(
                    '\n*{} hand of card: {}  *\n',
                    [cls.__actual_player, cls.__actual_player.hand_of_cards])

            elif cls.__actual_player.choosen_action == 'Steal':  ## STEAL
                Target_number = cls.__choosen_player_to_attack()
                counter = cls.__counter_action()
                if counter[0] == True:
                    Console.print_str_with_args(
                        '\n*{} counter-atack with {} *\n', [
                            cls.__players[counter[1]],
                            cls.__players[counter[1]].choosen_action
                        ])

                    challenge = cls.__ask_actual_player_to_challenge()
                    if challenge == True:
                        cls.__challenge(cls.__players[counter[1]],
                                        cls.__actual_player)
                    else:
                        cls.__Captain_act(cls.__actual_player, cls.__players[Target_number])
                        Console.print_str_with_args(
                            '\n*{} steal some coins, he has {} coins now *\n',
                            [cls.__actual_player, cls.__actual_player.coins])
                else:
                    cls.__Captain_act(cls.__actual_player,cls.__players[Target_number])
                    Console.print_str_with_args(
                        '\n*{} steal some coins, he has {} coins now *\n',
                        [cls.__actual_player, cls.__actual_player.coins])

            Console.clear()

    @classmethod
    def __counter_action(cls):

        counteratackking = [False, 0]
        counter_actions = [
            'Block-Foreign Aid', 'Block-Stealing', 'Block-Assassination'
        ]
        Console.clear()
        Console.print_str("     *  COUNTERING PHASE  * \n")
        for i in range(len(cls.__players)):
            if cls.__players[i] != cls.__actual_player:
                while True:
                    answer = Console.get_str_input_with_args(
                        '\n* {}, do you want to counter {}  * [ Yes / No ] \n',
                        [cls.__players[i].name, cls.__actual_player.name])
                    if answer == 'Yes' or answer == 'No':
                        if answer == 'Yes':
                            while True:
                                Console.print_str('\n * SELECT YOU COUNTER *\n  ')
                                Console.print_list(counter_actions)
                                counteraction = Console.get_str_input('')
                                if counteraction in counter_actions:
                                    cls.__players[
                                        i].choosen_action = counteraction
                                    counteratackking[0] = True
                                    counteratackking[1] = i
                                    break
                                else:
                                    Console.print_str(
                                        '* Wrong counter, please choose again * \n'
                                    )
                            break
                        elif answer == 'No':
                          break

                    else:
                        Console.print_str('\n * You answer isn´t valid * \n')
        return counteratackking

    @classmethod
    def __choosen_player_to_attack(cls):
        targets = []
        for i in range(len(cls.__players)):
            if cls.__players[i] != cls.__actual_player:
                targets.append(cls.__players[i].name)

        Console.print_str('* SELECT YOUR TARGET * \n\n')
        Console.print_list(targets)
        while True:       
            target = Console.get_str_input('')
            if target in targets:
                break
            else:
                Console.print_str("Wrong name, try again.")

        Console.print_str_with_args('\n* You selected {} *\n', [target])

        for number in range(len(cls.__players)):
            if cls.__players[i].name == target:
                return number

    ### Ending Phase Funtions
    @classmethod
    def __check_actual_player(cls):
        NUMBER = 0
        for i in range(cls.NUMBER_OF_PLAYERS):
            if len(cls.__players[i].hand_of_cards) == 0:
                Console.clear()
                Console.print_str_with_args("{}, has been eliminated",[cls.__players[i]])
                cls.NUMBER_OF_PLAYERS -=1
                Console.clear()
                cls.__players.remove(cls.__players[i])

            if cls.__players[i].number == cls.__actual_player.number:
                NUMBER = i

        if NUMBER == (cls.NUMBER_OF_PLAYERS - 1):
            cls.__actual_player = cls.__players[0]
        else:
            cls.__actual_player = cls.__players[NUMBER + 1]

    @classmethod
    def __clean_choseen_actions(cls):
        for i in range(len(cls.__players)):
            cls.__players[i].choosen_action = ''
        
    ### Actions of the influence 
    @classmethod
    def __Duke_act(cls, player):
        player.coins += 3

    @classmethod
    def __Ambassador_act(cls, player, deck):

        player.hand_of_cards.append(deck.pick_card_and_remove())
        player.hand_of_cards.append(deck.pick_card_and_remove())
        cards = []
        for card in player.hand_of_cards:
            cards.append(card)

        Console.print_list(cards)

        while True:
            discard1 = Console.get_str_input(
                ' * Select the first card that do you want to discard *\n')
            if discard1 in cards:
                break
            else:
                Console.print_str(
                    '* Wrong selection, please choose again * \n')

        deck.return_to_deck(discard1)
        cards.remove(discard1)

        while True:
            discard2 = Console.get_str_input(
                ' * Select the second card that do you want to discard *\n')
            if discard2 in cards:
                break
            else:
                Console.print_str(
                    '* Wrong selection, please choose again * \n')

        deck.return_to_deck(discard2)
        cards.remove(discard2)
        player.hand_of_cards = []

        for i in range(len(cards)):
            player.hand_of_cards.append(cards[i])

        Console.print_str(str(player.hand_of_cards))

    @classmethod
    def __Assassin_act(cls, player, target, deck):

        player.coins -= 3
        cards = []
        for card in target.hand_of_cards:
            cards.append(card)

        Console.print_list(cards)

        if len(cards)==2:
            while True:
                discard = Console.get_str_input(
                    ' * Select the first card that do you want to discard *\n')
                if discard in cards:
                    break
                else:
                    Console.print_str(
                        '* Wrong selection, please choose again * \n')
        else:
            discard = cards[0]

        target.hand_of_cards.remove(discard)
        cls.__Table.append(discard)

    @classmethod
    def __Captain_act(cls, player, target):
        if target.coins == 1:
            target.coins -= 1
            player.coins += 1
        elif target.coins == 0:
            pass
        else:
            target.coins -= 2
            player.coins += 2

    @classmethod
    def __Income(cls, player):
        player.coins += 1

    @classmethod
    def __Foreign_aid(cls, player):
        player.coins += 2

    @classmethod
    def __Coup(cls, player, target, deck):
        player.coins -= 7

        cards = []
        for card in target.hand_of_cards:
            cards.append(card)

        Console.print_str_with_args(
            "  *{}'s hands of cards *  ", [target])
        Console.print_list(cards)
        if len(cards)==2:
            while True:
                discard = Console.get_str_input(
                    ' * Select the card that do you want to discard *\n')
                if discard in cards:
                    break
                else:
                    Console.print_str(
                        '* Wrong selection, please choose again * \n')
        else:
            discard = cards[0]
      
        
        target.hand_of_cards.remove(discard)
        cls.__Table.append(discard)
