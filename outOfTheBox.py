from random import randint, choice

class boxes:
    # Rules
    # There are 5 boxes (but let's make this number variable)
    # The cat is in one of them
    # Each turn, you may (must) open one box and check to see if the cat is in it
    # If you find the cat, the game is over
    # After your turn, the cat will move to another adjecent box
    # The game is about the lowest number of turns to find the cat

    count = 0 # Class variable
    def __init__(self, numberOfBoxes = 5):
        if numberOfBoxes < 3: # Parameter variable
            numberOfBoxes = 3 # Need at least 3 boxes for the code to work
        self.numberOfBoxes = numberOfBoxes # Instance variable
        self.catInBox = randint(1, numberOfBoxes)
        self.catHistory = [self.catInBox] # Start a list with one item
        self.numTries = 0
        self.catFound = False
        boxes.count = boxes.count + 1 # Increase the class variable
        print("")
        print("Round " + str(boxes.count) + ". The cat has chosen a box to hide in.")

    def openBox(self, boxNumber):
        if self.catFound: # If we're done, we're done
            print("You've already found the cat in box " + str(self.catInBox) + ".")
        else:
            self.numTries = self.numTries + 1 
            if boxNumber == self.catInBox:
                msg = "The cat is here! You've found the cat in " + str(self.numTries) + " tries."
                self.catFound = True
            else:
                msg = "The cat is not here."
                if self.catInBox == 1:
                    self.catInBox = self.catInBox + 1
                elif self.catInBox == self.numberOfBoxes:
                    self.catInBox = self.catInBox - 1
                else:
                    self.catInBox = self.catInBox + choice([-1, 1])
                self.catHistory.append(self.catInBox)

            print("You open box number " + str(boxNumber) + ". " + msg)
        
        return self.catFound

    def whereHasTheCatBeen(self):
        print ("The cat has been in the following boxes: " + str( self.catHistory))

for tries in range(100):
    foundTheCat = False

    d = boxes(5)
    while not foundTheCat:
        foundTheCat = d.openBox(randint(1, 5))

    d.whereHasTheCatBeen()
