import random as r

#--------------------- KLASA MONET ------------------------------------------
class Monety(object):
    dostepnosc_monety = []
    nominaly = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    for i in range(30):
        x = r.choice(nominaly)
        dostepnosc_monety.append(x)
    dostepnosc_monety.sort(reverse = True)
    print("\nMonety dostępne w automacie to:\n")
    print(dostepnosc_monety)

    def __init__(self): #self - przez to kazdy obiekt jest widziany sam przez siebie, nazwa self winna byc pierwszym argumentem wszystkich deklarowanych metod
        dostepnosc_monety = self.dostepnosc_monety

    def dodaj_monety(self, moneta):
        self.dostepnosc_monety.append(moneta)
        print(self.dostepnosc_monety)

    def bierz_monety(self, nominal):
        self.dostepnosc_monety.remove(nominal)

#--------------------- KLASA PRODUKTOW ------------------------------------------
class Produkty(object):
    asortyment = [[30, 4.51, 5], [31, 1.10, 5], [32, 4.35, 5], [33, 5.0, 5], [34, 0.55, 5],
                  [35, 5.20, 5], [36, 8.0, 5], [37, 6.20, 5], [38, 4.25, 5], [39, 5.10, 5],
                  [40, 2.60, 5], [41, 4.15, 5], [42, 7.50, 5], [43, 5.25, 5], [44, 1.60, 1],
                  [45, 2.0, 5], [46, 5.52, 5], [47, 8.0, 5], [48, 0.75, 5], [49, 1.90, 5], [50, 1.05, 5]]

    def podaj_cene(self, numer): 
        for x in range(len(self.asortyment)):
            if self.asortyment[x][0] == numer:
                return self.asortyment[x][1]

    def podaj_ilosc(self, numer):
        for x in range(len(self.asortyment)):#len - pokazuje ilosc znakow w stringu
            if self.asortyment[x][0] == numer:
                return self.asortyment[x][2]
    print("\nAsortyment w automacie to:\n")
    print(asortyment)
    
    #--------------------- KLASA DO OBSLUGI AUTOMATU ------------------------------------------
class Obsluga_automatu(Produkty, Monety):

    def __init__(self, numer):
        self.numer = numer

    def sprawdz(self):
        if self.numer not in range(30, 51):  #range - to nie generator
            daj = 0
        else:
            x = Produkty.podaj_ilosc(self, self.numer)
            if x != 0:
                daj = 1
            else:
                daj = 2
        return daj

   def usun_asortyment(self):
        for x in range(len(self.asortyment)):
            if self.asortyment[x][0] == self.numer:
                self.asortyment[x][2] = self.asortyment[x][2] - 1
        print("Napój zostal usuniety!")
