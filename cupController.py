#This is a generic controller for the Cup() class implemented
#in useful_methods.py 


from useful_methods import *

def printInstructions():

		print("############################################################")
		print("")
		print("Instruction/Command List: "
		print("")
		print("   Type 'Roll' or 'roll' to roll all the die in the cup.")
		print("   Type 'display' or 'Display' to show all the faces.")
		print("")
		print("############################################################")
		

cup = Cup(10, 6)
state = True

while state == True:

		command = input("Please type a command: ")
		
		if command == "quit" or command == "Quit":
		
				state = False

	