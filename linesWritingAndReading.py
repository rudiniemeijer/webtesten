fileName = 'test.txt'
linebreak = '\n'

def getLinesFromFile():
    try:
       file = open(fileName, "r")
    except:
        return []

    listOfLines = []
    for line in file:
        listOfLines.append(line.strip(linebreak))

    file.close()
    return listOfLines

def writeLinesToFile(listOfLines):
    try:
        file = open(fileName, "w")
    except:
        return False

    for line in listOfLines:
        file.write(line + linebreak)

    file.close()
    return True

regels = ['hallo', 'welkom', 'test123']
writeLinesToFile(regels)
regels = getLinesFromFile()

volgNr = 0
for regel in regels:
    volgNr = volgNr + 1
    print(volgNr, regel)
