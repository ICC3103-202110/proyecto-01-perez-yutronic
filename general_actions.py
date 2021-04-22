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