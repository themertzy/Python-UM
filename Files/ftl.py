
#This function can be used to read in a file and split it along a certain

#designated delimeter. I have found this particularly usefull when dealing

#with lists of items in a file that require the replacement of a common delimeter.

#Note: This program returns a list of the items split at the given delimeter. If this

#delimeter is a new line character or something of that sort, then the delimeter

#needs to be put in with quotes. ALWAYS PUT FILE NAMES IN QUOTES!!!


#This function returns False if it fails to open, read, or split the text.


def ftl(inputFile, delimeter):

        try:

                with open(inputFile, "r") as myfile:

                        data = myfile.read().replace(delimeter, ' ')

                        returnValue = data.split(' ')

        except:
        
                returnValue = False
                
        return returnValue


