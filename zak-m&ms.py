import random
import string
alphabet = []
string.ascii_lowercase = alphabet

def makeMnmBagList(mnmQuan:int = 1):
    colors = ["oranje", "blauw", "groen", "bruin"]
    bag = []
    for i in range(mnmQuan):
        colorNum = random.randint(0, 3)
        bag.append(colors[colorNum])
    return bag

def makeMNmBagDict(mnmQuan:int = 1):    
    bag = {
        "oranje" : 0,
        "blauw" : 0,
        "groen" : 0,
        "bruin" : 0
    }
    for i in range(mnmQuan):
        colorNum = random.randint(0, 3)
        if colorNum == 0 :
            bag["oranje"] += 1
        if colorNum == 1 :
            bag["blauw"] += 1
        if colorNum == 2 :
            bag["groen"] += 1
        if colorNum == 3 :
            bag["bruin"] += 1
    return bag

def sortBag(collection:type):
    if type(collection) == list:
        sortlist = list()
        for i in collection:
            if i == "oranje":
                sortlist.append(i)
        for i in collection:
            if i == "blauw":
                sortlist.append(i)
        for i in collection:
            if i == "groen":
                sortlist.append(i)
        for i in collection:
            if i == "bruin":
                sortlist.append(i)
        return sortlist
    elif type(collection) == dict:
        return collection



    return collection 


def start():
    quantity = str(input("Hoeveel M&M's wil je? >>"))

    for i in range(len(quantity)):
        if quantity[i] in alphabet: print("Voer geen nummer in alstublieft"); start()
    if float(quantity) % 1 != 0: print("Voer een heel getal in"); start()
    else: quantity = int(quantity)
    listType(quantity)

def listType(quantity):
    colType = input("Wil je de lijst zien als een list of dict? L/D >>")

    if colType.lower() == "d": bag = makeMNmBagDict(quantity)
    elif colType.lower() == "l": bag = makeMnmBagList(quantity)
    bag = sortBag(bag)

    print(bag)

start()
input()