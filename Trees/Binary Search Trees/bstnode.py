class Node:

    def __init__(self, val):

        self.val = val

        self.leftChild = None

        self.rightChild = None

    def getVal(self):

        return self.val

    def setVal(self, val):

        self.val = val

    def getChildren(self):

        children = []

        if(self.leftChild != None):

            children.append(self.leftChild)

        if(self.rightChild != None):

            children.append(self.rightChild)

        return children
