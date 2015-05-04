from useful_methods import httpServer



command = input("Enter a command: ")

while True:

        if command=="start":

                httpServer()

        elif command=="stop":

                break
                

        command = input("Enter a command: ")
