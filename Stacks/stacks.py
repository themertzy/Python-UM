#This is a generic stack class. I have found that it is very useful in the representation
#of how computers internally work as well as being good to have for various list-esk
#problems. FYI many programing language interpreters and virtual machines are run
#using stacks of some form or another.

class Stack:

		def __init__(self, maxSize):
		
				self.stack = []
				self.maxSize = maxSize

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
				
