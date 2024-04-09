import random

class Hangman:
    lista = ["bagdad", "mosul", "basra", "arbil", "najaf", "dohuk"]

    """returnera ett slumpmässigt ord från listan"""
    @staticmethod
    def slump(listan):
        return random.choice(listan)
    #print(random.choice(lista)) # skriv ut lista i slumpmässig ordning
    #print(len(random.choice(lista))) # skriv ut hur många bokstäver ordet består av

    """Detta visar ordet personen har gissat."""
    @staticmethod
    def visa_ord(ordet, gissa):
        resultat = ""
        for bokstav in ordet:
            if bokstav in gissa:
                resultat += bokstav
            else:
                resultat += "_"
        return resultat

    """Spelets funktion"""
    def spelet(self):
        ordet = Hangman.slump(Hangman.lista)
        gissa = set()
        fel = 0
        max_fel = 6

        print("Välkommen till spelet Hangman, Gissa ordet", len(ordet), "bokstäver")

        """Regler för att spelet ska fungerar correkt"""
        while True:
            gissar = input("Gissa bokstav")

            if len(gissar) != 1:
               print("Du får bara ange en bokstav åt gången")
               continue

            if gissar in gissa:
               print("Du har redan gissat den bokstaven")
               continue

            if gissar in ordet:
               print("Bra!, denna bokstav finns i ordet")
               gissa.add(gissar)  # Add guessed letter to the set
            else:
                fel += 1
                print(f"Tyvärr!, denna {gissar} bokstav finns inte med i ordet")
                print(f"Du har {max_fel - fel} försök kvar att gissa ordet")

            print(Hangman.visa_ord(ordet, gissa))  # Display current state of the word

            if "_" not in Hangman.visa_ord(ordet, gissa):
                print(f"Grattis! Du gissade hela ordet: {ordet}")

            if fel >= max_fel:
                print(f"Tyvärr, Spelet är över. Ordet var: {ordet}")

if __name__ == "__main__":
    hangman_game = Hangman()  # Create an instance of the Hangman class
    hangman_game.spelet()  # Call the spelet() method to start the game