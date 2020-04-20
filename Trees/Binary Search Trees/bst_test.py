
#create a new emptry tree

tree = BST()

#creates 8 nodes in the tree with values between 1 and 25

for i in range (1,9):

    tree.insert(random.randint(1,25))

#search the tree

for i in range(1,10):

    #check to see if there are nodes with values from 1 to 9 in the tree

    found = tree.find(i)

    print(i, found)

    
