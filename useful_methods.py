#This file is a collection of useful functions that I have found that I often need.
#While most of them are very simple, some of them can be used for more complex tasks.
#All needed modules are imported with each function, class, or method.

##################################################################################################################################################################################

#This function can be used to read in a file and split it along a certain
#designated delimeter. I have found this particularly usefull when dealing
#with lists of items in a file that require the replacement of a common delimeter.
#Note: This program returns a list of the items split at the given delimeter. If this
#delimeter is a new line character or something of that sort, then the delimeter
#needs to be put in with quotes. ALWAYS PUT FILE NAMES IN QUOTES!!!
#This function was tested using the fileToTest.py and using the text file
#fileToTest.txt

#This function returns False if it fails to open, read, or split the text.

def fileToList(inputFile, delimeter):

        try:
                with open(inputFile, "r") as myfile:

                        data = myfile.read().replace(delimeter, ' ')

                        returnValue = data.split(' ')

        except:

                returnValue = False



        return returnValue
        

##################################################################################################################################################################################

#This is a class designed to create a die with n number of sides. You must initialize
#this class with a positive integer number of sides. A generic controller can be found
#in dieController.py

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


##################################################################################################################################################################################

#This is a generic stack class. I have found that it is very useful in the representation
#of how computers internally work as well as being good to have for various list-esk
#problems. FYI many programing language interpreters and virtual machines are run
#using stacks of some form or another. A test for this class can be found in 
#stackTest.py

class Stack:

		def __init__(self, maxSize):
		
				self.stack = []
				maxSize = maxSize

		def isEmpty(self):
		
				return len(self.stack) == 0

		def size(self):

				return len(self.stack)
				
		def push(self, item):  #puts an item on the top of the stack (aka the item at
							   #position '0'

			while len(self.stack) < maxSize:
		
				self.stack.insert(0, item)


		def pop(self):  #this method removes the top item (i.e. the item at position '0'
						#and returns it. Note that this item is not re-put back on the 
						#stack. This method does not work if there are no items on the 
						#stack. Although this may seem obvious, I decided to put this
						#check in place just for the sake of being thourough.

			while len(self.stack) != 0:
				
				self.topItem = self.stack[0]
		
				self.stack.remove(self.stack[0])
				
				return self.topItem
				
		def top(self):  #returns the top of the stack. Sometimes this method is refered 
						#to as the peek() method.
		
				return self.stack[0]
				

		def clear(self):  #this method clears all items out of the stack.

				self.stack=[]
				
##################################################################################################################################################################################

#This is a queue class.  Similar to the previously defined stack class, queue allows a user
#to put things on the top of the stack and take them off the bottom. This class can be extended
#to fit a wider range of problems.

class Queue:

		def __init__(self, maxSize):

				self.queue = []
				maxsize = maxSize

		def isEmpty(self):

				return len(self.queue) == 0

		def size(self):

				return len(self.queue)

		def push(self, itemToPush):

			while len(self.queue) < maxSize:

				self.queue.append(itemToPush)

		def pop(self):

			while len(self.queue) != 0:

				topItem = self.queue[0]

				self.queue.remove(self.queue[0])

				return topItem

		def last(self):

				return self.queue[0]

		def first(self):

				return self.queue[len(self.queue)-1]

##################################################################################################################################################################################

#Reverse Polish Notation (RPN) Calculator

#This calculator is stack based and supports the following operations:
#exponents, multiplication, division, addition, subtraction

#A test for this calculator can be found in rpnCalcTest.py

def op_pow(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a ** b )
def op_mul(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a * b )
def op_div(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a / b )
def op_add(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a + b )
def op_sub(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a - b )
def op_num(stack, num):
    stack.append( num )
 
ops = {
 '^': op_pow,
 '*': op_mul,
 '/': op_div,
 '+': op_add,
 '-': op_sub,
 }
 
def get_input(inp = None):
    'Inputs an expression and returns list of tokens'
 
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    return tokens
 
def rpn_calc(tokens):
    stack = []
    table = ['TOKEN,ACTION,STACK'.split(',')]
    for token in tokens:
        if token in ops:
            action = 'Apply op to top of stack'
            ops[token](stack)
            table.append( (token, action, ' '.join(str(s) for s in stack)) )
        else:
            action = 'Push num onto top of stack'
            op_num(stack, eval(token))
            table.append( (token, action, ' '.join(str(s) for s in stack)) )
    return table


##################################################################################################################################################################################

#This class is a controller for the Python defined dictionary class. This class
#is designed with simplicity in mind, making managing Python dictionaries much
#easier.

class PyDict:

	def __init__(self):						#Initializes an empty dictionary

		self.storage = {}


	def find(self, keyRep):					#Search for all the key values asscociated with the given key. 
											#Returns False if not found.

		if keyRep in storage:

			return self.storage[keyRep]

		else:

			return False


	def add(self, addKey, addVal):

		try:

			self.storage[addKey] = addVal

		except:


			return False


	def remove(self, delKey):

		try:

			del self.storage[delKey]

		except:

			return False


	def length(self):

		return len(self.storage)


	







					
		
				
