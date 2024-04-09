import random

class Hangman:
    lista = ["Bagdad", "Mosul", "Basra", "Arbil", "Najaf", "Dohuk"]

    #returnera ett slumpmässigt ord från listan
    def slump(self):
        return random.choice(lista)
    print(random.choice(lista)) # skriv ut lista i slumpmässig ordning


