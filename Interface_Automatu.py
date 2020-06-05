from tkinter import *
import System_Automatu as system
import Wyjatki as wyjatek

#--------------------- KLASA TKINTER ------------------------------------------
class Tkinter(object):
    
    """Klasy Tkinter
    ZMIENNE:
    *przycisk - zatwierdzenie kliknietego przycisku -> komunikat,
    *moneta - sluzy do wrzucania monet, sumuje,
    *obliczam_roznice - oblicza różnice pomiędzy kwota zaplaconą przez klienta a kwotą produktu z asortymentu."""
    
    wypisz = ''
    wrzucone = '0'
    cena = '0'
    lista = []
    numer = '0'
    roznica = '0'
    d = 0

    def __init__(self):
        self.wypisz = Tkinter.wypisz
        self.wrzucone = Tkinter.wrzucone
        self.cena = Tkinter.cena
        self.lista = Tkinter.lista
        self.roznica = Tkinter.roznica
        self.d = system.ObslugaAutomatu(self.numer)
        self.g = system.Monety()

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
        
        """Obsluga przyciskow funkcyjnych:
        ZMIENNE:
        *przycisk_tak - inaczej mówiąc przycisk zielony tzw. 'tik', 'fajka', informuje klienta, o cenie wybranego produktu, oraz podaje klarowny komunikat o wrzucenie pieniędzy za towar, jeśli produkt jest nie dostępny prosi by klient sprawdził dostępnosc danego produktu bądź tez czy wybral poprawny numer z listy asortymentu,
        *przycisk_sprawdz - informuje klienta, gdy podal zly numer wybranego przez siebie produktu, następnie sprawdza dostepnosć produktu - informuje o braku lub dostępności produktu w asortymencie i podaje cene tego produktu,
        *przycisk_do_czyszczenia - inaczej mówiąc przycisk czerwony X, służy do tzw. resetowania programu od początku, tzn. jeśli klient wybrał produkt i wplacil za niego cześć pieniędzy badz też calość, to i tak w dowolnej chwili moze nacisnąć ten przycisk i zanulować transakcje, wtedy automat odda mu wrzucone pieniądze i powróci do stanu wyjściowego,
        *przycisk_do_zatwietdzania - niebieski przycisk ze słowem 'ZATWIERDZ', informuje klienta o tym ile zostalo mu jeszcze do zaplaty, oraz informuje o wydaniu produktu za który klient zaplacił"""

        self.numer = float(self.wypisz)
        self.d = system.ObslugaAutomatu(self.numer)
        if self.d.sprawdz() == 1:
            self.cena = str(self.d.podaj_cene(self.numer))
            self.wypisz = f'Cena wybranego produktu to: {self.cena} zł. \nWrzuć monety.'
            string.set(self.wypisz)
            self.wypisz = ""
        else:
            self.wypisz = "Nie mogę sprzedać tego produktu.\nSprawdź czy jest on dostępny \noraz czy wybrałeś dobry numer!"
            string.set(self.wypisz)
            raise wyjatek.BladNumeruLubBrakProduktu
    
    def przycisk_sprawdz(self):
        self.numer = float(self.wypisz)
        self.d = system.ObslugaAutomatu(self.numer)
        if self.d.sprawdz() == 0:
            self.wypisz = "Podałeś zły numer produktu, \nkliknij czerwony przycisk i spróbuj jescze raz!"
            string.set(self.wypisz)
            raise wyjatek.BlednyNumer()
        elif self.d.sprawdz() == 1:
            self.wypisz = "Produkt jest dostępny.\n"
            string.set(self.wypisz)
            self.cena = str(self.d.podaj_cene(self.numer))
            self.wypisz = f'{self.wypisz} Cena wybranego produktu to: {self.cena} zł.'
            string.set(self.wypisz)
            self.wypisz = ""
        elif self.d.sprawdz() == 2:
            self.wypisz = "Produkt jest niedostępny!"
            string.set(self.wypisz)
            raise wyjatek.ProduktWyprzedany()

    def przycisk_do_czyszczenia(self):
        self.wypisz = ""
        string.set(self.wypisz)
        if self.wrzucone is not "0":
            string.set("Zwracam wrzucone pieniądze!")
            self.wrzucone = "0"
        else:
            string.set(
                'Podaj numer z przedziału 30-50, a następnie co chcesz zrobić: \n *zielony przycisk - rozpoczecie zakupu;\n *czerwony - anulowanie zakupu; \n *niebieski - sprawdzenie dostepnosci towaru.')

    def przycisk_do_zatwietdzania(self):
        if float(self.wrzucone) < float(self.cena):
            brak = self.cena + "-" + self.wrzucone
            brak = str(round(eval(brak), 3))
            self.wypisz = f'Do zapłaty pozostało jeszcze: {brak} zł'
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

""" Dodaje fotografie asortymentu z pliku zdjecia, użyte następnie do wizualnego obrazowania automatu. """

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

""" Dodaje fotografie ikon - tło, monety z pliku zdjecia, użyte następnie do wizualnego obrazowania automatu. """

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

"""Tworzę duże pole do którego następnie wgram tlo by urozmaicic wizualnie automat. 
    *Label - sluży do wyświetlania elementówgraficznych lub tekstu - przyjmuje argumenty (window - uchwyt okna głównego, image - zdjęcie z pliku). """

#--------------------- POLE AUTOMATU 1 ------------------------------------------
pole_nr_1 = Label(window, image = picture_1)  #duze pole na ktorym wszystkie pozostale ikonki mamy
pole_nr_1.place(relwidth = 1, relheight = 1)  #relwidth - wstawiam wartosć dla szerokości (ustawiam ja) , relhight - wstawiam wartosć dla wysokości (ustawiam ja)

"""Tworzę ramki do wizualnego przedsawienia monet, ikon w automacie. """

#--------------------- RAMKI ------------------------------------------
ramka_nr_1 = Frame(window, width = 500, height = 500, cursor = "dot", background = "white") #window - okno, width, height - rozmiar ogólny, cursor = "dot" - ramka w ksztalcie kwadratu, background - ustawia kolor tła
ramka_nr_1.place(relx = 0.05, rely = 0.01, relwidth = 0.5, relheight = 0.3) #relx - polożenie poziome, rely - połozenie pionowe, relwidth - rozmiar szerokosć, relheight - rozmiar wysokosc
ramka_nr_2 = Frame(window, width = 500, height = 500, cursor = "circle", background = "black") #window - okno, width, height - rozmiar ogólny, cursor = "circle" - ramka w ksztalcie kola, background - ustawia kolor tła
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

"""Tworzę kolejne pola - pierwsze do informacji ogólnej co nalezy zrobic by rozpocząc transakcje, drugie do asortymentu. """

#--------------------- KOLEJNE POLE AUTOMATU 2 --------------------------------------
pole_nr_2 = Label(ramka_nr_1, background = "black", foreground = "white", font = ("Arial",18, "italic"), textvariable = string, anchor = CENTER) #background - kolor tła, foreground - kolor czcionki, font - czcionka jakiej uzywamy do wyświetlania tekstu , anchor - kontroluje gdzie ustawiamy np. tekst -> N, NE, E, SE, S, SW, W, NW, CENTER
pole_nr_2.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)  #relx - polożenie poziome, rely - połozenie pionowe, relwidth - rozmiar szerokosci, relheight - rozmiar wysokosci
pole_nr_3 = Label(ramka_nr_3, text = 'Napoje', font = ("Arial",23, "italic"), foreground="red", anchor = CENTER) #anchor - położenie tekstu tu akurat wysrodkowane, foreground - 
pole_nr_3.place(relwidth = 1, relheight = 1)

"""Tworzę kolejne pola - numerki dla danego zdj z asortymentu. """

#--------------------- NUMERKI DANEGO ASORTYMENTU--------------------------------------
pole_nr_4 = Label(ramka_nr_5, text = '30.      31.      32.     33.     34.      35.      36.      37.      38.      39.      40.', font = ("Arial",15), background = "pink", foreground="black")
pole_nr_4.place(relwidth = 1.009, relheight = 0.8)
pole_nr_5 = Label(ramka_nr_7, text = '  41.      42.        43.       44.        45.      46.        47.       48.        49.      50.', font = ("Arial",15), background = "pink", foreground="black")
pole_nr_5.place(relwidth = 1.009, relheight = 0.8)

"""Tworzę przyciski do wrzucania monet i ustalam obsługe ich kliknięcia, oraz tytuł, rodzaj i wielkosc czcionki w tytule
borderwidth -szerokośc obramowania, activebackground - kolor pierwszoplanowy, text - tekst do wyswietlania"""
#--------------------- PRZYCISKI --------------------------------------
przycisk_1gr = Button(ramka_nr_2, text = "1grosz", borderwidth = 0, command = lambda: tk.moneta(0.01), font = ("Arial", 50), image = jeden_grosz, activebackground = "black", background = "black") 
przycisk_2gr = Button(ramka_nr_2, text = "2grosze", borderwidth = 0, command = lambda: tk.moneta(0.02), font = ("Arial", 50), image = dwa_grosze, activebackground = "black", background = "black") 
przycisk_5gr = Button(ramka_nr_2, text = "5groszy", borderwidth = 0, command = lambda: tk.moneta(0.05), font = ("Arial", 50), image = piec_groszy, activebackground = "black", background = "black") 
przycisk_10gr = Button(ramka_nr_2, text = "10groszy", borderwidth = 0, command = lambda: tk.moneta(0.1), font = ("Arial", 50), image = dziesiec_groszy, activebackground = "black", background = "black") 
przycisk_20gr = Button(ramka_nr_2, text = "20groszy", borderwidth = 0, command = lambda: tk.moneta(0.2), font = ("Arial", 50), image = dwadziescia_groszy, activebackground = "black", background = "black") 
przycisk_50gr = Button(ramka_nr_2, text = "50groszy", borderwidth = 0, command = lambda: tk.moneta(0.5), font = ("Arial", 50), image = piecdziesiat_groszy, activebackground = "black", background = "black") 
przycisk_1zl = Button(ramka_nr_2, text = "1zł", borderwidth = 0, command = lambda: tk.moneta(1.0), font = ("Arial", 50), image = jeden_zl, activebackground = "black", background = "black") 
przycisk_2zl = Button(ramka_nr_2, text = "2zł", borderwidth = 0, command = lambda: tk.moneta(2.0), font = ("Arial", 50), image = dwa_zl, activebackground = "black", background = "black") 
przycisk_5zl = Button(ramka_nr_2, text = "5zł", borderwidth = 0, command = lambda: tk.moneta(5.0), font = ("Arial", 50), image = piec_zl, activebackground = "black", background = "black") 

przycisk_tak = Button(ramka_nr_2, image = tak, background = "black", borderwidth = 0, command = tk.przycisk_tak)
przycisk_nie = Button(ramka_nr_2, image = nie, background = "black", borderwidth = 0, command = tk.przycisk_do_czyszczenia)
przycisk_sprawdz = Button(ramka_nr_2, text = "SPRAWDZ", font = 40, borderwidth = 0, background = "navy", foreground = "white", command = tk.przycisk_sprawdz)
przycisk_do_zatwietdzania = Button(ramka_nr_2, text = "ZATWIERDZ", font = 40, borderwidth = 0, background = "green", foreground = "white", command = tk.przycisk_do_zatwietdzania)

przycisk_nr_0 = Button(ramka_nr_2, text = "0", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(0))
przycisk_nr_1 = Button(ramka_nr_2, text = "1", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(1))
przycisk_nr_2 = Button(ramka_nr_2, text = "2", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(2))
przycisk_nr_3 = Button(ramka_nr_2, text = "3", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(3))
przycisk_nr_4 = Button(ramka_nr_2, text = "4", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(4))
przycisk_nr_5 = Button(ramka_nr_2, text = "5", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(5))
przycisk_nr_6 = Button(ramka_nr_2, text = "6", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(6))
przycisk_nr_7 = Button(ramka_nr_2, text = "7", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(7))
przycisk_nr_8 = Button(ramka_nr_2, text = "8", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(8))
przycisk_nr_9 = Button(ramka_nr_2, text = "9", font = 40, borderwidth = 0, activebackground = "grey", command = lambda: tk.przycisk(9))

przycisk_1gr.place(relx = 0.72, rely = 0.67, relwidth = 0.10, relheight = 0.10)
przycisk_2gr.place(relx = 0.72, rely = 0.56, relwidth = 0.10, relheight = 0.10)
przycisk_5gr.place(relx = 0.72, rely = 0.45, relwidth = 0.10, relheight = 0.10)
przycisk_10gr.place(relx = 0.72, rely = 0.34, relwidth = 0.10, relheight = 0.10)
przycisk_20gr.place(relx = 0.72, rely = 0.23, relwidth = 0.10, relheight = 0.10)
przycisk_50gr.place(relx = 0.72, rely = 0.12, relwidth = 0.10, relheight = 0.10)
przycisk_1zl.place(relx = 0.84, rely = 0.48, relwidth = 0.10, relheight = 0.10)
przycisk_2zl.place(relx = 0.84, rely = 0.37, relwidth = 0.10, relheight = 0.10)
przycisk_5zl.place(relx = 0.84, rely = 0.26, relwidth = 0.10, relheight = 0.10)

przycisk_tak.place(relx = 0.08, rely = 0.8, relwidth = 0.1, relheight = 0.1)
przycisk_nie.place(relx = 0.5, rely = 0.8, relwidth = 0.1, relheight = 0.1)
przycisk_sprawdz.place(relx = 0.08, rely = 0.9, relwidth = 0.52, relheight = 0.05)
przycisk_do_zatwietdzania.place(relx = 0.66, rely = 0.9, relwidth = 0.3, relheight = 0.05)

przycisk_nr_0.place(relx = 0.3, rely = 0.7, relwidth = 0.1, relheight = 0.1)
przycisk_nr_1.place(relx = 0.1, rely = 0.1, relwidth = 0.1, relheight = 0.1)
przycisk_nr_2.place(relx = 0.3, rely = 0.1, relwidth = 0.1, relheight = 0.1)
przycisk_nr_3.place(relx = 0.5, rely = 0.1, relwidth = 0.1, relheight = 0.1)
przycisk_nr_4.place(relx = 0.1, rely = 0.3, relwidth = 0.1, relheight = 0.1)
przycisk_nr_5.place(relx = 0.3, rely = 0.3, relwidth = 0.1, relheight = 0.1)
przycisk_nr_6.place(relx = 0.5, rely = 0.3, relwidth = 0.1, relheight = 0.1)
przycisk_nr_7.place(relx = 0.1, rely = 0.5, relwidth = 0.1, relheight = 0.1)
przycisk_nr_8.place(relx = 0.3, rely = 0.5, relwidth = 0.1, relheight = 0.1)
przycisk_nr_9.place(relx = 0.5, rely = 0.5, relwidth = 0.1, relheight = 0.1)

""" Dodaje fotografie asortymentu - produkty z pliku zdjecia, użyte następnie do wizualnego obrazowania automatu oraz ponizej ustalam pozycje i miejsce gdzie maja się znajdować """
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

if __name__ == '__main__': #dopisanie linijki kodu do blokowania wyswietlania okna automatu podczas odpalania testow jednostkowych
    window.mainloop()
