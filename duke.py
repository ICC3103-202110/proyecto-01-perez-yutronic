class Duke:
    def Duke_act(self,coins):
        self.coins += 3
        self.player.cards.remove("Duke")
        deck.extend("Duke")
        self.player.cards.extend([deck.pop()])
    
    def Duke_block(self,player,coins,action):
        if self.action == player.Foreign_ad:
            self.player.coins += 0