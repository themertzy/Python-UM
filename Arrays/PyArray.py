class PyArray:

    def __init__(self, *argv):

        self.mainArray = []

        if len(argv) >= 0:
        
            for arg in argv:

                self.mainArray.append(arg)

    def add(self, *argv):

        for arg in argv:

            self.mainArray.append(arg)

    def insert(self, item, pos):

        self.item = item
        self.pos = pos

        return None

    def delete(self):

        return None

    def clear(self):

        self.mainArray = []

    def show(self):

        return self.mainArray

    def findItem(self):

        return None

    def findAll(self):

        return None



