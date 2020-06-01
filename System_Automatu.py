import random as rnd
from tkinter import *

#--------------------- KLASA MONET ------------------------------------------
class Monety(object):
    
    """Klasa Monet służy do reprezentacji tzw. skarbca na pieniądze.
    ZMIENNE:
    *NOMINALY - to zmienna odpowiedzialna za przechowywanie monet,
    METODY:
    *dodaj_monety - dodaje monety do skarbca na pieniądze oraz sprawdza dostępność danego nominału 
    *bierz_monety - wydaje monety ze skarbca na pieniądze oraz sprawdza dostępność danego nominału """
    
    dostepnosc_monety = []
    NOMINALY = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    for i in range(30):
        x = rnd.choice(NOMINALY)
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
    
    """Klasa Produktów służy do reprezentacji asortymentu.
    ZMIENNE:
    *ASORTYMENT - to zmienna odpowiedzialna za przechowywanie produktów dostępnych w automacie. Są tu przechowywane takie informacje jak: numer produktu, cena produktu oraz ilość danego produktu w calym asortymencie.
    METODY:
    *podaj_cene - zwraca cene produktu o danym numerze,
    *podaj_ilosc - zwraca ilosc danego produktu o danym numerze."""

    ASORTYMENT = [[30, 4.51, 5], [31, 1.10, 5], [32, 4.35, 5], [33, 5.0, 5], [34, 0.55, 5],
                  [35, 5.20, 5], [36, 8.0, 5], [37, 6.20, 5], [38, 4.25, 5], [39, 5.10, 5],
                  [40, 2.60, 5], [41, 4.15, 5], [42, 7.50, 5], [43, 5.25, 5], [44, 1.60, 1],
                  [45, 2.0, 5], [46, 5.52, 5], [47, 8.0, 5], [48, 1.00, 5], [49, 1.90, 5], [50, 1.05, 5]]

    def podaj_cene(self, numer): 
        for x in range(len(self.ASORTYMENT)):
            if self.ASORTYMENT[x][0] == numer:
                return self.ASORTYMENT[x][1]

    def podaj_ilosc(self, numer):
        for x in range(len(self.ASORTYMENT)):#len - pokazuje ilosc znakow w stringu
            if self.ASORTYMENT[x][0] == numer:
                return self.ASORTYMENT[x][2]
    print("\nAsortyment w automacie to:\n")
    print(ASORTYMENT)
    
#--------------------- KLASA DO OBSLUGI AUTOMATU ------------------------------------------
class ObslugaAutomatu(Produkty, Monety):
    
    """Klasa do obslugi automatu służy do obslugi maszyny.
    METODY:
    *sprawdz - sprawdza ilosc danego asortymentu,
    *usun_asortyment - służy do usunięcia zakupionego towaru z asortymentu,
    *reszta - wydaje reszte za zakupiony towar, wyciąga monety ze skarbca na pieniądze lub informuje klienta by wrzucił odliczoną kwote, gdy nie jest w stanie wydać reszty. """
    
    def __init__(self, numer):
        self.numer = numer

    def sprawdz(self):
        if not 30 <= self.numer <= 50:
            daj = 0
        else:
            x = Produkty.podaj_ilosc(self, self.numer)
            if x != 0:
                daj = 1
            else:
                daj = 2
        return daj

    def usun_asortyment(self):
        for x in range(len(self.ASORTYMENT)):
            if self.ASORTYMENT[x][0] == self.numer:
                self.ASORTYMENT[x][2] = self.ASORTYMENT[x][2] - 1
        print("Napój zostal usuniety!")
        
    def reszta(self, roznica):
        roznica = round(float(roznica), 3)#funkcja round () zwraca liczbe zmiennoprzecinkowa ktara jest zaokraglona wersja podanej liczby z okreslona liczba miejsc poprzecinku 
        i = 0
        pomocnicza = []
        dostepna_ilosc = sum(self.dostepnosc_monety)
        wypisz = ""
        j = True
        if roznica > dostepna_ilosc:
            wypisz = "Prosze wrzucic tylko odliczona kwote!"
            return wypisz
        else:
            while roznica > 0:
                if i < len(self.dostepnosc_monety):
                    if roznica >= self.dostepnosc_monety[i]:
                        roznica = round((roznica - self.dostepnosc_monety[i]), 3)
                        pomocnicza.append(self.dostepnosc_monety[i])
                        print(roznica)
                else:
                    wypisz = "Prosze wrzucic tylko odliczona kwote!"
                    pomocnicza = []
                    break
                i = i + 1
            for i in range(len(pomocnicza)):
                Monety.bierz_monety(self, pomocnicza[i])
                j = False
            print()
            print(self.dostepnosc_monety)
            wypisz = wypisz + "\n Reszta =  " + str(round(sum(pomocnicza), 3)) + " zł"
            return wypisz, j
#help(ObslugaAutomatu) #sprawdzenie działania help
