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