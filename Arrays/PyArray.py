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

    def removeItem(self, *argv):

        for arg in argv:

            return None        

        return None

    def removeItems(self, *argv):

        for arg in argv:

            return None

    def clear(self):

        self.mainArray = []

    def show(self):

        return self.mainArray

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



