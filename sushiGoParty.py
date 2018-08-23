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

cards = []

def makeCards():
    for card in cardList:
        for count in range(card[2]):
            cards.append(Cards(card))

class Player:

    count = 1

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

    def dealHand(self, size):
        random.shuffle(deck)
        for x in range(size):
            self.hand.append(deck.pop(0))

class Menue:

    def __init__(self):
        self.menue = []
        self.myFirstMeal = []

    def myFirstMeal(self):
        for card in cardList:
            if card.name in self.myFirstMeal:
                self.menue.append(card)

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

def playerCount():
    while True:
        playerCount = input('How many players? (2-8)')
        if isADigit(playerCount) == True and playerCount >= '2' and playerCount <= '8':
            playerCount = int(playerCount)
            playerGroup = []
            for x in range(playerCount):
                playerGroup.append(Player())
            return playerGroup
            break
        else:
            print('Please select a valid number of players.')

def gameMode():
    gameModes = ['My First Meal', 'Sushi Go!', 'Party Sampler', 'Master Menu', 'Points Platter', 'Cutthroat Combo', 'Big Banquet', 'Dinner For Two']
    while True:
        print('Which meal will you choose (1-8)?')
        modeChoice = listMaker(gameModes)
        if modeChoice in gameModes:
            modeChoice = int(gameModes.index(modeChoice))
            return modeChoice
            break
        else:
            print('Please select a valid game mode.')

def createDeck(gameMode):
    deck =[]
    if gameMode == 0:
        mode = ['Nigiri', 'Maki Roll', 'Tempura', 'Sashimi', 'Miso Soup', 'Wasabi', 'Tea', 'Green Tea Ice Cream']
        for card in cards:
            print(card)
            if card.name in mode:
                deck.append(card)
        return deck
    elif gameMode == 1:
        pass
    elif gameMode == 2:
        pass
    elif gameMode == 3:
        pass
    elif gameMode == 4:
        pass
    elif gameMode == 5:
        pass
    elif gameMode == 6:
        pass
    elif gameMode == 7:
        pass

def removeDessert():
    global deck
    dessertPile = []
    while deck[-1].foodType >= 20:
        dessertPile.append(deck[-1])
        deck.pop(-1)
    return dessertPile

def dessertAmount(playerCount, roundCount):
    if playerCount <= 5:
        if roundCount < 3:
            return 7 - (2*roundCount)
        else:
            return 2
    elif playerCount >= 6:
        return 9 - (2*roundCount)

def dealDessert(playerCount, roundCount):
    global dessertPile
    temp_deck = []
    amount = dessertAmount(playerCount, roundCount)
    for x in range(amount):
        print(x)
        temp_deck.append(dessertPile.pop(0))
    return temp_deck

def dealHand(playerCount):
    if playerCount == 8:
        amount = 7
    elif playerCount > 6:
        amount = 8
    elif playerCount > 4:
        amount = 9
    else:
        amount = 10
    for player in playerGroup:
        player.dealHand(amount)
            

def roundLoop(number):
    rotation = 0
    if number % 2 == 0:
        rotation = 1
    for player in playerGroup:
        player.chooseCard()

roundCount = 1
playerGroup = playerCount()
playerCount = len(playerGroup)
makeCards()
gameMode = gameMode()
deck = createDeck(gameMode)
dessertPile = removeDessert()
deck.extend(dealDessert(playerCount, roundCount))
dealHand(playerCount)

print(playerGroup)
print(gameMode)
print(deck)
print(dessertPile)

for player in playerGroup:
    print(player.hand)



        

    
    
    
