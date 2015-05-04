from useful_methods import *

def printInstructions():

		print("######################################")
		print("")
		print("   Type quit() to end the program.")
		print("")
		print("   Type fib() to enter Fibonacci mode.")
		print("")
		print("   Type help() to reprint instructions.")
		print("")
		print("######################################")

command = ""

printInstructions()

while command != "quit()":

		
		command = input("Please enter a command: ")
		print("")
		
		if command == "fib()":
		
				fibNum = int(input("Enter a number: "))
				print("")
				print("The Fibonacci number where n = " + str(fibNum) + " is " + str(fibonacci(fibNum)) + ".")
				print("")

