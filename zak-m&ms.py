import random
import string
alphabet = []
string.ascii_lowercase = alphabet
colors = ["oranje", "blauw", "groen", "bruin"]

def makeMnmBag(mnmQuan:int = 1):
    bag = []
    for i in range(mnmQuan):
        colorNum = random.randint(0, 3)
        bag.append(colors[colorNum])
    return bag

def start():
    quantity = str(input("Hoeveel M&M's wil je? >>"))

    for i in range(len(quantity)):
        if quantity[i] in alphabet: print("Voer geen nummer in alstublieft"); start()
    if float(quantity) % 1 != 0: print("Voer een heel getal in"); start()
    else: quantity = int(quantity)

    bag = makeMnmBag(quantity)
    for i in bag:
        print(f"Deze M&M is {i}")
start()
input()