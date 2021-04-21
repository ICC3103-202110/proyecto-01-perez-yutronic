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
