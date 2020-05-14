import random as r
from tkinter import *

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
        
#----------------------- WYJATKI ---------------------------------------------
class BladNumeruLubBrakProduktu(Exception):
    pass
class BlednyNumer(Exception):
    pass
class ProduktWyprzedany(Exception):
    pass
       
#--------------------- KLASA TKINTER ------------------------------------------
class Tkinter(object):
    wypisz = ''
    wrzucone = '0'
    cena = '0'
    lista = []
    numer = '0'
    roznica = '0'
    d = 0

    def __init__(self):
        wypisz = self.wypisz
        wrzucone = self.wrzucone
        cena = self.cena
        lista = self.lista
        roznica = self.roznica
        self.d = Obsluga_automatu(self.numer)
        self.g = Monety()

    def przycisk(self, num):
        self.wypisz = self.wypisz + str(num)
        string.set(self.wypisz)

    def moneta(self, num):
        self.wrzucone = self.wrzucone + "+" + str(num)
        self.wrzucone = str(round(eval(self.wrzucone), 3))
        string.set(self.wrzucone)
        self.lista.append(num)

    def obliczam_roznice(self):
        self.roznica = self.wrzucone + "-" + self.cena
        self.roznica = str(round(eval(self.roznica), 3))
        return self.roznica
    
#--------------------- OBSLUGA PRZYCISKOW FUNKCYJNYCH ------------------------------------------
    def przycisk_tak(self):
        self.numer = eval(self.wypisz)
        self.d = Obsluga_automatu(self.numer)
        if self.d.sprawdz() == 1:
            self.cena = str(self.d.podaj_cene(self.numer))
            self.wypisz = "Cena wybranego produktu to " + self.cena + " zł. \nWrzuć monety."
            string.set(self.wypisz)
            self.wypisz = ""
        else:
            self.wypisz = "Nie mogę sprzedać tego produktu.\nSprawdź czy jest on dostępny \nlub czy wybrałeś dobry numer."
            string.set(self.wypisz)
            raise BladNumeruLubBrakProduktu

    
    def przycisk_sprawdz(self):
        self.numer = eval(self.wypisz)
        self.d = Obsluga_automatu(self.numer)
        if self.d.sprawdz() == 0:
            self.wypisz = "Podałeś zły numer produktu, \nkliknij czerwony przycisk i spróbuj jescze raz."
            string.set(self.wypisz)
            raise BlednyNumer()
        elif self.d.sprawdz() == 1:
            self.wypisz = "Produkt jest dostępny.\n"
            string.set(self.wypisz)
            self.cena = str(self.d.podaj_cene(self.numer))
            self.wypisz = self.wypisz + "Cena wybranego produktu to " + self.cena + " zł."
            string.set(self.wypisz)
            self.wypisz = ""
        elif self.d.sprawdz() == 2:
            self.wypisz = "Produkt jest niedostępny."
            string.set(self.wypisz)
            raise ProduktWyprzedany()

    def przycisk_do_czyszczenia(self):
        self.wypisz = ""
        string.set(self.wypisz)
        if self.wrzucone is not "0":
            string.set("Zwracam wrzucone pieniądze.")
            self.wrzucone = "0"
        else:
            string.set(
                'Podaj numer (30-50) a następnie co chcesz zrobić \n Zielony przycisk - rozpoczecie zakupu\n Czerwony - anulowanie zakupu, \n Niebieski - sprawdzenie dostepnosci towaru')

    def przycisk_do_zatwietdzania(self):
        if float(self.wrzucone) < float(self.cena):
            brak = self.cena + "-" + self.wrzucone
            brak = str(round(eval(brak), 3))
            self.wypisz = "Do zapłaty pozostało jeszcze " + brak
            string.set(self.wypisz)
        if float(self.wrzucone) >= float(self.cena):
            self.wypisz = 'Wydawanie produktu.'
            string.set(self.wypisz)
            roz = Tkinter.obliczam_roznice(self)
            k = self.d.reszta(roz)
            string.set(self.wypisz + k[0])
            if k[1] == False:
                self.wrzucone = '0'
            self.d.usun_asortyment()
            for i in range(len(self.lista)):
                self.g.dodaj_monety(self.lista[i])
            print("Dodano monety.")
            self.lista = []
            self.wrzucone = '0'
            
#tworze glowne okno automatu
tk = Tkinter() 
window = Tk() 
window.title("Automat z napojami.")
HEIGHT = 800 #rozmiary okna 
WIDTH = 1400 #rozmiary okna
canva = Canvas(window, height=HEIGHT, width=WIDTH)
canva.pack()

#--------------------- ASORTYMENT ------------------------------------------
woda_niegazowana = PhotoImage(file = "zdjecia/woda_niegazowana.png")
woda_gazowana = PhotoImage(file = "zdjecia/woda_gazowana.png")
waterr = PhotoImage(file = "zdjecia/waterr.png")
zywiec_zdroj_woda_cytrynowa = PhotoImage(file = "zdjecia/zywiec_zdroj_woda_cytrynowa.png")
zywiec_zdroj_woda_truskawkowa = PhotoImage(file = "zdjecia/zywiec_zdroj_woda_truskawkowa.png")
zywiec_zdroj_woda_limonka_i_mieta = PhotoImage(file = "zdjecia/zywiec_zdroj_woda_limonka_i_mieta.png")
tymbark_h2o_malina = PhotoImage(file = "zdjecia/tymbark_h2o_malina.png")
tymbark_mieta_malina = PhotoImage(file = "zdjecia/tymbark_mieta_malina.png")
tymbark_mango_mieta = PhotoImage(file = "zdjecia/tymbark_mango_mieta.png")
tymbark_jablko_wisnia = PhotoImage(file = "zdjecia/tymbark_jablko_wisnia.png")
tymbark_jablko_kiwi = PhotoImage(file = "zdjecia/tymbark_jablko_kiwi.png")
kubus_banan_jablko_marchewka = PhotoImage(file = "zdjecia/kubus_banan_jablko_marchewka.png")
kubus_mango_brzoskwinia_banan = PhotoImage(file = "zdjecia/kubus_mango_brzoskwinia_banan.png")
smoothie_truskawka_jablko = PhotoImage(file = "zdjecia/smoothie_truskawka_jablko.png")
coca_cola = PhotoImage(file = "zdjecia/coca_cola.png")
pepsi = PhotoImage(file = "zdjecia/pepsi.png")
fanta = PhotoImage(file = "zdjecia/fanta.png")
mirynda = PhotoImage(file = "zdjecia/mirynda.png")
sprite = PhotoImage(file = "zdjecia/sprite.png")
tiger = PhotoImage(file = "zdjecia/tiger.png")
black = PhotoImage(file = "zdjecia/black.png")

#--------------------- STRUKTURA IKON ------------------------------------------
picture_1 = PhotoImage(file = "zdjecia/tlo.png")
tak = PhotoImage(file = "zdjecia/tak.png")
nie = PhotoImage(file = "zdjecia/nie.png")
jeden_grosz = PhotoImage(file = "zdjecia/1grosz.png")
dwa_grosze = PhotoImage(file = "zdjecia/2grosze.png")
piec_groszy = PhotoImage(file = "zdjecia/5groszy.png")
dziesiec_groszy = PhotoImage(file = "zdjecia/10groszy.png")
dwadziescia_groszy = PhotoImage(file = "zdjecia/20groszy.png")
piecdziesiat_groszy = PhotoImage(file = "zdjecia/50groszy.png")
jeden_zl = PhotoImage(file = "zdjecia/1zl.png")
dwa_zl = PhotoImage(file = "zdjecia/2zl.png")
piec_zl = PhotoImage(file = "zdjecia/5zl.png")
string = StringVar()
string.set(
    'Podaj numer (30-50) a następnie co chcesz zrobić'
    '\n Zielony przycisk - rozpoczecie zakupu'
    '\n Czerwony - anulowanie zakupu,'
    '\n Niebieski - sprawdzenie dostepnosci towaru')

#--------------------- POLE AUTOMATU 1 ------------------------------------------
pole_nr_1 = Label(window, image = picture_1)  #duze pole na ktorym wszystkie pozostale ikonki mamy
pole_nr_1.place(relwidth = 1, relheight = 1)

#--------------------- RAMKI ------------------------------------------
ramka_nr_1 = Frame(window, width = 500, height = 500, cursor = "dot", background = "white")
ramka_nr_1.place(relx = 0.05, rely = 0.01, relwidth = 0.5, relheight = 0.3)
ramka_nr_2 = Frame(window, width = 500, height = 500, cursor = "dot", background = "black")
ramka_nr_2.place(relx = 0.6, rely = 0, relwidth = 0.4, relheight = 1)
ramka_nr_3 = Frame(window, width = 500, height = 500, cursor = "dot", background = "white")
ramka_nr_3.place(relx = 0.05, rely = 0.33, relwidth = 0.50, relheight = 0.1)
ramka_nr_4 = Frame(window, width = 500, height = 500, cursor = "dot", background = "white")
ramka_nr_4.place(relx = 0.05, rely = 0.44, relwidth = 0.5, relheight = 0.45)
ramka_nr_5 = Frame(window, width = 500, height = 500, cursor = "dot", background = "pink")
ramka_nr_5.place(relx = 0.05, rely = 0.610, relwidth = 0.5, relheight = 0.04)
ramka_nr_6 = Frame(window, width = 500, height = 500, cursor = "dot", background = "white")
ramka_nr_6.place(relx = 0.05, rely = 0.645, relwidth = 0.5, relheight = 0.02)
ramka_nr_7 = Frame(window, width = 500, height = 500, cursor = "dot", background = "pink")
ramka_nr_7.place(relx = 0.05, rely = 0.8665, relwidth = 0.5, relheight = 0.04)

#--------------------- KOLEJNE POLE AUTOMATU 2 --------------------------------------
pole_nr_2 = Label(ramka_nr_1, bg = "black", foreground = "white", font = ("Arial",23, "italic"), textvariable = string, anchor = CENTER)
pole_nr_2.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
pole_nr_3 = Label(ramka_nr_3, text = 'Napoje', font = ("Arial",23, "italic"), foreground="red")
pole_nr_3.place(relwidth = 1, relheight = 1)

#--------------------- NUMERKI DANEGO ASORTYMENTU--------------------------------------
pole_nr_4 = Label(ramka_nr_5, text = '30.      31.      32.     33.     34.      35.      36.      37.      38.      39.      40.', font = ("Arial",15), background = "pink", foreground="black")
pole_nr_4.place(relwidth = 1.009, relheight = 0.8)
pole_nr_5 = Label(ramka_nr_7, text = '  41.      42.        43.       44.        45.      46.        47.       48.        49.      50.', font = ("Arial",15), background = "pink", foreground="black")
pole_nr_5.place(relwidth = 1.009, relheight = 0.8)

#--------------------- PRZYCISKI --------------------------------------
przycisk_1gr = Button(ramka_nr_2, text = "1grosz", command = lambda: tk.moneta(0.01), font = ("Arial", 50), image = jeden_grosz, background = "black", foreground = "white") 
przycisk_2gr = Button(ramka_nr_2, text = "2grosze", command = lambda: tk.moneta(0.02), font = ("Arial", 50), image = dwa_grosze, background = "black", foreground = "white") 
przycisk_5gr = Button(ramka_nr_2, text = "5groszy", command = lambda: tk.moneta(0.05), font = ("Arial", 50), image = piec_groszy, background = "black", foreground = "white") 
przycisk_10gr = Button(ramka_nr_2, text = "10groszy", command = lambda: tk.moneta(0.1), font = ("Arial", 50), image = dziesiec_groszy, background = "black", foreground = "white") 
przycisk_20gr = Button(ramka_nr_2, text = "20groszy", command = lambda: tk.moneta(0.2), font = ("Arial", 50), image = dwadziescia_groszy, background = "black", foreground = "white") 
przycisk_50gr = Button(ramka_nr_2, text = "50groszy", command = lambda: tk.moneta(0.5), font = ("Arial", 50), image = piecdziesiat_groszy, background = "black", foreground = "white") 
przycisk_1zl = Button(ramka_nr_2, text = "1zł", command = lambda: tk.moneta(1.0), font = ("Arial", 50), image = jeden_zl, background = "black", foreground = "white") 
przycisk_2zl = Button(ramka_nr_2, text = "2zł", command = lambda: tk.moneta(2.0), font = ("Arial", 50), image = dwa_zl, background = "black", foreground = "white") 
przycisk_5zl = Button(ramka_nr_2, text = "5zł", command = lambda: tk.moneta(5.0), font = ("Arial", 50), image = piec_zl, background = "black", foreground = "white") 

przycisk_tak = Button(ramka_nr_2, image = tak, background = "black", borderwidth = 0, command = tk.przycisk_tak)
przycisk_nie = Button(ramka_nr_2, image = nie, background = "black", borderwidth = 0, command = tk.przycisk_do_czyszczenia)
przycisk_sprawdz = Button(ramka_nr_2, text = "SPRAWDZ", font = 40, borderwidth = 0, background = "navy", foreground = "white", command = tk.przycisk_sprawdz)
przycisk_do_zatwietdzania = Button(ramka_nr_2, text = "ZATWIERDZ", font = 40, borderwidth = 0, background = "green", foreground = "white", command = tk.przycisk_do_zatwietdzania)

przycisk_1gr.place(relx = 0.79, rely = 0.77, relwidth = 0.10, relheight = 0.10)
przycisk_2gr.place(relx = 0.79, rely = 0.66, relwidth = 0.10, relheight = 0.10)
przycisk_5gr.place(relx = 0.79, rely = 0.55, relwidth = 0.10, relheight = 0.10)
przycisk_10gr.place(relx = 0.79, rely = 0.44, relwidth = 0.10, relheight = 0.10)
przycisk_20gr.place(relx = 0.79, rely = 0.33, relwidth = 0.10, relheight = 0.10)
przycisk_50gr.place(relx = 0.79, rely = 0.22, relwidth = 0.10, relheight = 0.10)
przycisk_1zl.place(relx = 0.90, rely = 0.58, relwidth = 0.10, relheight = 0.10)
przycisk_2zl.place(relx = 0.90, rely = 0.47, relwidth = 0.10, relheight = 0.10)
przycisk_5zl.place(relx = 0.90, rely = 0.36, relwidth = 0.10, relheight = 0.10)

przycisk_tak.place(relx = 0.08, rely = 0.8, relwidth = 0.1, relheight = 0.1)
przycisk_nie.place(relx = 0.5, rely = 0.8, relwidth = 0.1, relheight = 0.1)
przycisk_sprawdz.place(relx = 0.08, rely = 0.9, relwidth = 0.52, relheight = 0.05)
przycisk_do_zatwietdzania.place(relx = 0.66, rely = 0.9, relwidth = 0.3, relheight = 0.05)

#--------------------- ZDJECIA - ASORTYMENT --------------------------------------
zdjecie_1 = Label(ramka_nr_4, image = woda_niegazowana)
zdjecie_2 = Label(ramka_nr_4, image = woda_gazowana)
zdjecie_3 = Label(ramka_nr_4, image = waterr)
zdjecie_4 = Label(ramka_nr_4, image = zywiec_zdroj_woda_cytrynowa)
zdjecie_5 = Label(ramka_nr_4, image = zywiec_zdroj_woda_truskawkowa)
zdjecie_6 = Label(ramka_nr_4, image = zywiec_zdroj_woda_limonka_i_mieta)
zdjecie_7 = Label(ramka_nr_4, image = tymbark_h2o_malina)
zdjecie_8 = Label(ramka_nr_4, image = tymbark_mieta_malina)
zdjecie_9 = Label(ramka_nr_4, image = tymbark_mango_mieta)
zdjecie_10 = Label(ramka_nr_4, image = tymbark_jablko_wisnia)
zdjecie_11 = Label(ramka_nr_4, image = tymbark_jablko_kiwi)
zdjecie_12 = Label(ramka_nr_4, image = kubus_banan_jablko_marchewka)
zdjecie_13 = Label(ramka_nr_4, image = kubus_mango_brzoskwinia_banan)
zdjecie_14 = Label(ramka_nr_4, image = smoothie_truskawka_jablko)
zdjecie_15 = Label(ramka_nr_4, image = coca_cola)
zdjecie_16 = Label(ramka_nr_4, image = pepsi)
zdjecie_17 = Label(ramka_nr_4, image = fanta)
zdjecie_18 = Label(ramka_nr_4, image = mirynda)
zdjecie_19 = Label(ramka_nr_4, image = sprite)
zdjecie_20 = Label(ramka_nr_4, image = tiger)
zdjecie_21 = Label(ramka_nr_4, image = black)

zdjecie_1.place(relx = 0.01, rely = 0.01, relwidth = 0.08, relheight = 0.35)
zdjecie_2.place(relx = 0.10, rely = 0.015, relwidth = 0.07, relheight = 0.35)
zdjecie_3.place(relx = 0.19, rely = 0.015, relwidth = 0.07, relheight = 0.35)
zdjecie_4.place(relx = 0.28, rely = 0.015, relwidth = 0.07, relheight = 0.355)
zdjecie_5.place(relx = 0.37, rely = 0.015, relwidth = 0.07, relheight = 0.355)
zdjecie_6.place(relx = 0.46, rely = 0.015, relwidth = 0.07, relheight = 0.345)
zdjecie_7.place(relx = 0.55, rely = 0.015, relwidth = 0.065, relheight = 0.349)
zdjecie_8.place(relx = 0.64, rely = 0.015, relwidth = 0.065, relheight = 0.349)
zdjecie_9.place(relx = 0.73, rely = 0.015, relwidth = 0.065, relheight = 0.349)
zdjecie_10.place(relx = 0.82, rely = 0.015, relwidth = 0.065, relheight = 0.349)
zdjecie_11.place(relx = 0.92, rely = 0.015, relwidth = 0.061, relheight = 0.349)
zdjecie_12.place(relx = 0.01, rely = 0.45, relwidth = 0.07, relheight = 0.52)
zdjecie_13.place(relx = 0.11, rely = 0.455, relwidth = 0.07, relheight = 0.52)
zdjecie_14.place(relx = 0.21, rely = 0.45, relwidth = 0.07, relheight = 0.52)
zdjecie_15.place(relx = 0.31, rely = 0.45, relwidth = 0.08, relheight = 0.52)
zdjecie_16.place(relx = 0.41, rely = 0.45, relwidth = 0.07, relheight = 0.52)
zdjecie_17.place(relx = 0.51, rely = 0.45, relwidth = 0.08, relheight = 0.52)
zdjecie_18.place(relx = 0.615, rely = 0.45, relwidth = 0.08, relheight = 0.52)
zdjecie_19.place(relx = 0.715, rely = 0.45, relwidth = 0.08, relheight = 0.52)
zdjecie_20.place(relx = 0.81, rely = 0.45, relwidth = 0.08, relheight = 0.52)
zdjecie_21.place(relx = 0.91, rely = 0.45, relwidth = 0.08, relheight = 0.52)
