#This is a class designed to create a die with n number of sides. You must initialize
#this class with a positive integer number of sides.

import random

class Die:
        
        def __init__(self, numberOfSides): 
                
                self.numSides = int(numberOfSides)
                self.currentFace = None

        def roll(self):
                
            self.currentFace = random.randrange(1, self.numSides)                

        def displayFace(self):

            return self.currentFace

        def changeNumberOfSides(self, newNum): #newNum is an integer.

                self.numSides = newNum

        def displayNumberOfSides(self): #returns an integer

                return self.numSides

##################################################################################################################################################################################

#This is a class designed to handle n number of Die() as a group, or cup.  This allows
#the user to roll all the die at once or freeze certain ones so that they do not roll
#while the others do.

#Both of the next two imports are simply in place in case you decide to copy and paste 
#the code into another program instead of importing the class or the whole useful_methods.py
#file.

#A generic controller for this class can be found in cupController.py

#NOTE: The previously defined Die() class is needed for this class to work correctly.


#Previously Imported-----------------------------------------------------------------------------------
#import random

class Cup:

		def __init__(self, numberOfDie, numberOfSides):
		
				#Creates a list of lists. Each position in self.cup contains a list with
				#a Die() and a False. The False is used for determining whether or not
				#a Die() is frozen. Every Die() starts off as not being frozen and with
				#the same number of sides.
		
				self.numSides = int(numberOfSides)
				self.numDie = int(numberOfDie)
				self.cup = []
				
				
				for i in range(0, self.numDie-1):

						self.workingArray = []
				
						self.workingArray.append(Die(self.numSides))
						self.workingArray.append(False)
				
						self.cup.append(self.workingArray)
						
						
						
		def rollCup(self):
		
				for g in range(0, self.numDie-1):
				
						if self.cup[g][1] == False:
						
								self.cup[g][0].roll()
								
		def displayFaces(self): 

				#This method returns a list of the current faces of the each Die() in the cup.
		
				self.currentFaces = []
				
				for h in range(0, self.numDie-1):

						self.currentFaces.append(self.cup[h][0].displayFace())

				return self.currentFaces

		def freeze(self, pos):

				#This method freezes a Die() at position = pos in the Cup(), effectively preventing that Die() 
				#from being rolled. This is done by changing the freeze variable for that particular Die() 
				#to True. This method does not return a value.

				self.cup[pos][1] = True

		def isFrozenOneDie(self, pos):

				#Returns True if the Die() at position = pos in the Cup()
				#is frozen and False if not.

				return self.cup[pos][1]

		def displayNumberOfSidesOneDie(self, pos):

				#This method returns the number of sides of the Die() in the Cup() at position = pos.

				return self.cup[pos][0].displayNumberOfSides()

		def changeNumberOfSidesOneDie(self, pos, newSideNum):

				#Changes the number of sides for a Die() in the Cup() at position = pos

				self.cup[pos][0].changeNumberOfSides(newSideNum)

		def displayAllNumberOfSides(self):

				#Returns a list of all the current Die() number of sides.

				allSides = []

				for pos in range(0, self.numDie-1):

						allSides.append(self.cup[pos][0].displayNumberOfSides())

				return allSides

		def changeAllNumberOfSides(self, newSideNum):

				#Changes the number of sides for all the Die() in the Cup()
				#to newSideNum

				for pos in range(0, self.numDie-1):

						self.cup[pos][0].changeNumberOfSides(newSideNum)

		def freezeAll(self):

				#freezes all the Die() in the Cup() at one time.

				for pos in range(0, self.numDie-1):

						self.cup[pos][1] = True

		def isAllFrozen(self):

				#Returns a list of all the frozen states of all the Die() in the Cup()

				totalFrozen = []

				for pos in range(0, self.numDie-1):

						totalFrozen.append(self.cup[pos][1])

				return totalFrozen
