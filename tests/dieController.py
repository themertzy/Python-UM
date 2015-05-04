from ..useful_methods import *

#The useful_methods.py is required for this die generator to work correctly.

def printInstructions():

    print("##############################################################################################")
    print("")
    print("Instructions: ")
    print("")
    print("   Type 'change' or 'Change' to change the number of sides for the die of the current session.")
    print("   Type 'roll' or 'Roll' to roll the die.")
    print("   Type 'Quit' or 'quit' to end the current session of the generator.")
    print("   Type 'sides' or 'Sides' to view the current number of sides.")
    print("   To reprint the instructions type 'Instructions' or 'instructions'")
    print("")
    print("##############################################################################################")
    print("")

printInstructions()
num = input("Please enter the number of sides for your die: ")
print("")

numInt = int(num)
Die = Die(numInt)



while True:

    command = input("Enter a command: ")
    print("")

    if command == "roll" or command == "Roll":

        Die.roll()
        print("Current Face: " + str(Die.displayFace()))
        print("")

    elif command == "change" or command == "Change":

        x = input("How many sides would you like the current die to have? ")
        Die.changeNumberOfSides(int(x))
        print("Number of sides changed to " + str(Die.displayNumberOfSides()))
        print("")

    elif command == "sides" or command == "Sides":

        print("Current Number of Sides: " + str(Die.displayNumberOfSides()))
        print("")

    elif command == "instructions" or command == "Instructions":

        printInstructions()

    elif command == "quit" or "Quit":

        break

    else:

        print("Invalid Command.")
        print("")
