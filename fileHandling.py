fileName = 'test.txt'
linebreak = '\n'

def getItemsFromFile():
    try:
       file = open(fileName, "r")
    except:
        return []

    listOfItems = []
    for item in file:
        listOfItems.append(item.strip(linebreak).split(', '))

    file.close()
    return listOfItems

def writeItemsToFile(listOfItems):
    try:
        file = open(fileName, "w")
    except:
        return False

    for item in listOfItems:
        file.write((', '.join(map(str, item))) + linebreak)

    file.close()
    return True

items = [['a,99,22'], ['b,34,dd'], ['c,5,21']]
writeItemsToFile(items)
items = getItemsFromFile()
print(items)
