import random

class Hangman:
    lista = ["bagdad", "mosul", "basra", "arbil", "najaf", "dohuk"]

    #returnera ett slumpmässigt ord från listan
    def slump(self):
        return random.choice(lista)
    print(random.choice(lista)) # skriv ut lista i slumpmässig ordning
    print(len(random.choice(lista))) # skriv ut hur många bokstäver ordet består av


