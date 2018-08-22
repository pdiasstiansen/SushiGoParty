import random

class Cards:

    def __init__(self):
        self.name = ''
        self.type = 0
        self.food = 0

cardList = []

class Player:

    count = 1

    def __init__(self):
        self.hand = ['ba','dsfsd', 'asas']
        self.board = []
        self.points = 0
        self.name = 'player' + str(Player.count)
        Player.count += 1

    def __repr__(self):
        return self.name

    def chooseCard(self):
        choice = listMaker(self.hand)
        
        

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
        print('bla')
        return True
    print('ol')
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
    for index, choice in enumerate(listOfChoices):
        print(str(index + 1) + ' - ' + str(choice))
    while True:#Here--------------------------------------------------------------
        choice = input()
        choice = selection(listOfChoices, choice)
        if choice == 'Cancel' and cancel == True:
            return True
        elif choice in listOfChoices:
            return choice
            print('You must select a valid option')
        else:
            print('You must select a valid option')

while True:
    playerCount = input('How many players? (2-8)')
    if isADigit(playerCount) == True and playerCount >= '2' and playerCount <= '8':
        playerCount = int(playerCount)
        playerGroup = []
        for x in range(playerCount):
            playerGroup.append(Player())
        print(playerGroup)
        break
    else:
        print('Please select a valid number of players.')

def roundLoop(number):
    rotation = 0
    if number % 2 == 0:
        rotation = 1
    for player in playerGroup:
        player.chooseCard()

roundLoop(1)



        

    
    
    
