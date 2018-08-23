import random

class Cards:

    def __init__(self, card):
        self.name = card[0]
        self.foodType = card[1]

    def __repr__(self):
        return self.name

cardList = [['Nigiri', 0, 12],
            ['Maki Roll', 1, 12],
            ['Temaki', 2, 12],
            ['Uramaki', 3, 12],
            ['Tempura', 4, 8],
            ['Sashimi', 5, 8],
            ['Dumpling', 6, 8],
            ['Eel', 7, 8],
            ['Tofu', 8, 8],
            ['Onigiri', 9, 8],
            ['Edamame', 10, 8],
            ['Miso Soup', 11, 8],
            ['Chopsticks', 12, 3],
            ['Soy Sauce', 13, 3],
            ['Tea', 14, 3],
            ['Menu', 15, 3],
            ['Spoon', 16, 3],
            ['Special Order', 17,3],
            ['Takeout Box', 18, 3],
            ['Wasabi', 19, 3],
            ['Pudding', 20, 15],
            ['Green Tea Ice Cream', 21, 15],
            ['Fruit', 22, 15]]

class Player:

    playerCount = 0
    count = 1 # end of game need to reset this to empty list
    playerGroup = [] # end of game need to reset this to empty list

    def __init__(self):
        self.hand = []
        self.board = []
        self.points = 0
        self.name = 'player' + str(Player.count)
        Player.count += 1

    def __repr__(self):
        return self.name

    def chooseCard(self):
        choice = listMaker(self.hand)

    def dealHand(self):
        temp_handSize = self.handAmount()##move this elsewhere, it only needs to be run after player ammount is chosen
        print(temp_handSize)
        print(len(menue.menue))
        for x in range(temp_handSize):
            self.hand.append(menue.menue.pop(0))

    def handAmount(self):
        if Player.playerCount == 8:
            return 7
        elif Player.playerCount > 6:
            return 8
        elif Player.playerCount > 4:
            return 9
        else:
            return 10

class Menue:

    def __init__(self):
        self.menue = []
        self.dessert = []
        self.myFirstMealList = ['Nigiri', 'Maki Roll', 'Tempura', 'Sashimi', 'Miso Soup', 'Wasabi', 'Tea', 'Green Tea Ice Cream']

    def pickMeal(self):
        pass
        
    def myFirstMeal(self):
        for card in game.cards:
            if card.name in self.myFirstMealList and card.foodType < 20:
                self.menue.append(card)
                print(card)
        for card in game.cards:
            if card.name in self.myFirstMealList and card.foodType >= 20:
                self.dessert.append(card)
                print('Dessert: ' , card)
        self.dealDessert()

    ##Put rest of meal codes here

    def dessertAmount(self, playerCount, roundCount):
        if playerCount <= 5:
            if roundCount < 3:
                return 7 - (2*roundCount)
            else:
                return 2
        elif playerCount >= 6:
            return 9 - (2*roundCount)

    def dealDessert(self):
        amount = self.dessertAmount(Player.playerCount, game.roundCount)
        for x in range(amount):
            temp_cardToAdd = self.dessert.pop(0)
            self.menue.append(temp_cardToAdd)
        random.shuffle(self.menue)

class Game:

    def __init__(self):
        self.mode = 0
        self.roundCount = 1
        self.cards = []

    def pickMode(self):
        gameModes = ['My First Meal', 'Sushi Go!', 'Party Sampler', 'Master Menu', 'Points Platter', 'Cutthroat Combo', 'Big Banquet', 'Dinner For Two']
        while True:
            print('Which meal will you choose (1-8)?')
            modeChoice = listMaker(gameModes)
            if modeChoice in gameModes:
                modeChoice = int(gameModes.index(modeChoice))
                self.mode = modeChoice
                break
            else:
                print('Please select a valid game mode.')

    def createDeck(self):
        if self.mode == 0:
            menue.myFirstMeal()
        elif self.mode == 1:
            pass
        elif self.mode == 2:
            pass
        elif self.mode == 3:
            pass
        elif self.mode == 4:
            pass
        elif self.mode == 5:
            pass
        elif self.mode == 6:
            pass
        elif self.mode == 7:
            pass

    def playerCount(self):
        while True:
            playerCount = input('How many players? (2-8)')
            if isADigit(playerCount) == True and playerCount >= '2' and playerCount <= '8':
                Player.playerCount = int(playerCount)
                print(Player.playerCount)
                for x in range(Player.playerCount):
                    Player.playerGroup.append(Player())
                break
            else:
                print('Please select a valid number of players.')

    def makeCards(self):
        for card in cardList:
            for count in range(card[2]):
                self.cards.append(Cards(card))
        
                

def isADigit(digit):
    if type(digit) == int:
        return True
    if digit.isdigit() == True:
        return True
    else:
        return False

def selection(listOfChoices, selection):
    if isADigit(selection) == False:
        return False
    else:
        try:
            return listOfChoices[int(selection) - 1]
        except:
            return None

def listMaker(listOfChoices):
    while True:
        for index, choice in enumerate(listOfChoices):
            print(str(index + 1) + ' - ' + str(choice))
        choice = input()
        choice = selection(listOfChoices, choice)
        if choice == 'Cancel' and cancel == True:
            return True
        elif choice in listOfChoices:
            return choice
            print('You must select a valid option')
        else:
            print('You must select a valid option')
            

def roundLoop(number): # integrate into game class
    rotation = 0
    if number % 2 == 0:
        rotation = 1
    for player in playerGroup:
        player.chooseCard()

game = Game()
menue = Menue()
game.playerCount()
game.makeCards()
game.pickMode()
game.createDeck()
print('playerGroupsize: ' , len(Player.playerGroup)) 
for player in Player.playerGroup:
    player.dealHand()


for player in Player.playerGroup:
    print(player.hand)



        

    
    
    
