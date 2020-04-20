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

