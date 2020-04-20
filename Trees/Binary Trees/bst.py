class BST:

    def __init__(self):

        self.root = None

    def setRoot(self,val):

        self.root = Node(val)

    def insert(self, val):

        #mutator method to add a node to the sree 

        if(self.root is None):

            self.setRoot(val)

        else:

            self.__insertNode(self.root, val)

    def __insertNode(self, currentNode, val):

        #private method to create a node

        if(val <= currentNode.getVal()):

            if(currentNode.leftChild):

                self.__insertNode(currentNode.leftChild, val)

            else:

                currentNode.leftChild = Node(val)

        elif(val > currentNode.val):

            if(currentNode.rightChild):

                self.__insertNode(currentNode.rightChild, val)

            else:

                currentNode.rightChild = Node(val)

    def find(self, val):

        #accessor method to find and return a node's value

        return self.__findNode(self.root, val)

    def __findNode(self, currentNode, val):

        #private method to return the value from a node

        if(currentNode is None):

            return False

        elif(val == currentNode.val):

            return True

        elif(val < currentNode.val):

            return self.__findNode(currentNode.leftChild, val)

        else:

            return self.__findNode(currentNode.rightChild, val)
