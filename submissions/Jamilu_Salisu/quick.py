def printEvenNumbers(startingNumber, endingNumber):
    if startingNumber < endingNumber:
        for i in range(startingNumber, endingNumber):
            if i % 2 == 0:
                print(i)
    else:
        print("Starting number must be less than ending number")

printEvenNumbers(11, 100)


##
def cleanString(text):
    return text

def name(name):
    print("Greetings, " + name)

name("Jamilu Salisu")