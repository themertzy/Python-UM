class PyArray:

    def __init__(self, *argv):

        self.mainArray = []

        if len(argv) > 0:
        
            for arg in argv:

                self.mainArray.append(arg)

    def add(self):

        return None

    def delete(self):

        return None

    def clear(self):

        self.mainArray = []

    def clone(self):

        return self.mainArray

