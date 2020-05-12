class PyArray:

    def __init__(self, *argv):

        self.mainArray = []

        if len(argv) >= 0:
        
            for arg in argv:

                self.mainArray.append(arg)

    def add(self, *argv):

        for arg in argv:

            self.mainArray.append(arg)

    def change(self, item, pos):

        self.item = item
        self.pos = pos

        self.mainArray[self.pos] = self.item

    def removeItem(self, item):

        self.item = item

        for i in self.mainArray:

            if self.mainArray[i] == self.item:
                
                self.mainArray.remove(self.item)    

                return self.item

    def removeItems(self, *argv):

        for arg in argv:

            if arg == self.mainArray[arg]:

                self.mainArray.remove(arg)

    def clear(self):

        self.mainArray = []

    def showAll(self):

        return self.mainArray
    
    def showOne(self, pos):
        
        return self.mainArray[pos]

    def size(self):

        return len(self.mainArray)

    def findItem(self, itemName):

        self.itemName = itemName

        for i in self.mainArray:

            if self.mainArray[i] == self.itemName:

                return self.mainArray[i]

    def findAll(self, itemName):

        self.itemName = itemName
        self.allItems = []

        for i in self.mainArray:

            if self.mainArray[i] == self.itemName:

                self.allItems.append(self.mainArray[i])

        return self.allItems



