import itertools
import random

class Cards:
    def __init__(self):
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.values = range(1,14)
        self.RealCards = []
        for Card in itertools.product(self.suits,self.values):
            self.RealCards,append(Card)
    def GetRandomCard(self):
        RandomNumber = random.randint(0,51)
        ReturnedCard = self.RealCards[RandomNumber]
    return(ReturnedCard)

class Player:
    def __init__(self, ID, Card):
        self.name = NameofGame

class War(Game):
    def __init__(self, NumberofPlayers):
        self.NumberofPlayers  = NumberofPlayers
        self.PlayerList = []
    def GameStart(self):
        CarDeck = Cards()
        for playerID in range(0, self.NumberofPlayers):
            PlayersCard = CarDeck.GetRandomCard()
            NewPlayer = Player(playerID, PlayersCard)
            self.PlayerList.append(NewPlayer)
        self.Winner()
    def Winner(self):
        WinningID = self.PlayerList[0]
        for playerID in self.PlayerList:
            if(playerID.PlayersCard[1] > WinningID.PlayersCard[1]):
                WinningID = playerID
        print("And the winner is... " + str(WinningID.playerID)
        print("The winning card was... " + str(WinningID.PlayersCard[1]) + " of " + str(WinningID.PlayersCard[0])

if __name__=="__main__":
    NewGame = SimpleWar(2)
    NewGame.StartGame()

            
