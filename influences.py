class General_actions:
    def Foreign_ad(self,player,coins):
        self.player.coins += 2
    
    def Income(self,player,coins):
        self.player.coins += 1
        
    def Coup(self,coins,player_selected,card_selected):
        self.player.coins -= 7
        print("Select a player to kill a influence...", input(self.player_selected))
        print(player_selected, "Choose a influence to delete...")
        c = str(input())
        player_selected.cards.remove(c)
        
    
class Influences:
    def __init__(self,turn,player,played_card,player_selected):
        self.turn = 1
        self.played_card = played_card
        self.player_selected = player_selected
        self.player = player


class Ambassador:
    def Ambassador_act(self,player,deck):
        self.player.cards.extend([deck.pop(),deck.pop()])
        print(self.player.cards)
        coord1 = input("Please write which two cards do you want to return to the deck, in format Card1,Card2: ").split(",")        
        c1,c2 = coord1[0],coord1[1]
        print("your chosed cards are: ", c1,c2)
        deck.append(c1),deck.append(c2)
        random.shuffle(deck,random.random)
        self.player.cards.remove(str(c1))
        self.player.cards.remove(str(c2))
        print(self.player.cards)

class Duke:
    def Duke_act(self,coins):
        self.coins += 3
        self.player.cards.remove("Duke")
        deck.extend("Duke")
        self.player.cards.extend([deck.pop()])
    
    def Duke_block(self,player,coins,action):
        if self.action == player.Foreign_ad:
            self.player.coins += 0
            
class Assassin:
    def Assasin_act(self,coins,player_selected,player):
        self.coins -= 3
        print("Choose a player...",self.player_selected = input()) #no se si poner player_selected o name
        c = str(input("Choose a card..."))
        self.player_selected.cards.remove(c)               #cambiar a player variable

class Captain:
    def Captain_act(self,player_selected):
        print("Choose a player...")
        if player_selected.coins == 1:
            self.player_selected.coins -= 1
        elif player_selected.coins == 0:
            pass
        else:
            player_selected.coins -= 2

    def Captain_block(self,player_selected): 