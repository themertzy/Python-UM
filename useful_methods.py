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

#A simple implementation of a Node class used in Binary Trees and Binary Search Trees.

class Node:
	
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	
	def __str__(self):
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	
	def __repr__(self):
		return str(self)
	
##################################################################################################################################################################################
#Binary Tree

class BinaryTree(obj):

	def __init__(self):

		self.left = None
		self.right = None
		self.data = None
	
	def add(self, addVal):
		
		return 0  #Expand this function
	
	def remove(self, removeVal):
		
		return 0  #Expand this function
	
	def size(self):
		
		return 0  #Expand this function

##################################################################################################################################################################################

#This class defines a Node on a given binary tree.  This class is required for the BinarySearchTree class.

class TreeNode:
	
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                   if self.isLeftChild():
                       succ = self.parent
                   else:
                       self.parent.rightChild = None
                       succ = self.parent.findSuccessor()
                       self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

##################################################################################################################################################################################

#A more broad approach to the Binary Search Tree.  This class requires the previously defined TreeNode class.

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)

    def remove(self,currentNode):
         if currentNode.isLeaf(): #leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #interior
           succ = currentNode.findSuccessor()
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # this node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else:
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else:
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)


##################################################################################################################################################################################

#Fibonacci Sequence Function using Recursion

def fibb_recur(n):
	
	if n <= 1:
		return n
	else:
		return(fibb_recur(n-1) + fibb_recur(n-2))

##################################################################################################################################################################################

#A Fibonacci Sequence Function using iteration.  Iteration is often considered to be slower than a recursive approach.

def fib_iteration(n):
    
	a = 0
	b = 1
    
	for i in range(0, n):
        	temp = a
        	a = b
        	b = temp + b
		
    	return a
