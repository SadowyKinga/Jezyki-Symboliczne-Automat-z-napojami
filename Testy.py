import unittest
import System_Automatu, Interface_Automatu, Wyjatki

class MyTestCase(unittest.TestCase):
    print("\nTESTY\n")
    #Test nr.1 - Sprawdzanie ceny jednego towaru - oczekiwana informacja o cenie
    def test_nr_1_informacja_o_cenie(self):
        self.assertEqual(System_Automatu.Produkty().podaj_cene(30), 4.51)

    #Test nr.2 - Wrzucenie odliczonej kwoty, zakup towaru - oczekiwany brak reszty
    def test_nr_2_odliczona_kwota(self):
        test_machine = Interface_Automatu.Tkinter()
        test_machine.moneta(1)
        test_machine.moneta(0.10)
        test_machine.przycisk(31)
        test_machine.przycisk_tak()
        self.assertEqual(test_machine.obliczam_roznice(), '0.0')

    #Test nr.3 - Wrzucenie wiekszej kwoty, zakup towaru - oczekiwana reszta
    def test_nr_3_większa_kwota_do_zaplaty(self):
        test_machine = Interface_Automatu.Tkinter()
        test_machine.moneta(4)
        test_machine.moneta(5)
        test_machine.przycisk(32)
        test_machine.przycisk_tak()
        self.assertEqual(test_machine.obliczam_roznice(), '4.65')
        
    #Test nr.4 - Wykupienie calego asortymentu,proba zakupu po wyczerpaniu towaru - oczekiwana informacja o braku
    #Test nr.4 - Wykupienie calego asortymentu,proba zakupu po wyczerpaniu towaru - oczekiwana informacja o braku
    def test_nr_4_wykupienie_calego_asortymentu(self):
        test_machine = Interface_Automatu.Tkinter()
        with self.assertRaises(Wyjatki.BlednyNumer):
            test_machine.przycisk(0)
            test_machine.przycisk_sprawdz()
            test_machine.przycisk(33)
            test_machine.moneta(5)
            test_machine.przycisk_tak()
            test_machine.przycisk(33)
            test_machine.moneta(5)
            test_machine.przycisk_tak()
            test_machine.przycisk(33)
            test_machine.moneta(5)
            test_machine.przycisk_tak()
            test_machine.przycisk(33)
            test_machine.moneta(5)
            test_machine.przycisk_tak()
            test_machine.przycisk(33)
            test_machine.moneta(5)
            test_machine.przycisk_tak()
            with self.assertRaises(Wyjatki.ProduktWyprzedany):
                test_machine.przycisk(33)
                test_machine.przycisk_sprawdz()
    
    #Test nr.5 - WSprawdzenie ceny towaru o nieprawidlowym numerze (<30 lub >50) - oczekiwana informacja o bledzie
    def test_nr_5_nieprawidlowy_numer(self):
        test_machine = Interface_Automatu.Tkinter()
        with self.assertRaises(Wyjatki.BlednyNumer):
            test_machine.przycisk(0)
            test_machine.przycisk_sprawdz()

    #Test nr.6 - Wrzucenie kilku monet, przerwanie transakcji - oczekiwany zwrot monet
    def test_nr_6_przerwanie_transakcji(self):
        test_machine = Interface_Automatu.Tkinter()
        test_machine.moneta(5)
        test_machine.moneta(2)
        test_machine.moneta(1)
        test_machine.przycisk_do_czyszczenia()
        
    #Test nr.7 - Wrzucenie za malej kwoty, wybranie poprawnego numeru towaru, wrzucenie reszty monet do odliczonej kwoty, ponowne wybranie poprawnego numeru towaru - oczekiwany brak reszty      
    def test_nr_7_mniejsza_kwota_do_zaplaty(self):
        test_machine = Interface_Automatu.Tkinter()
        test_machine.moneta(2)
        test_machine.moneta(2)
        test_machine.przycisk(46)
        test_machine.przycisk_tak()
        test_machine.moneta(1)
        test_machine.moneta(0.50)
        test_machine.moneta(0.02)
        test_machine.przycisk(46)
        test_machine.przycisk_tak()
        self.assertEqual(test_machine.obliczam_roznice(), '0.0')

    #Test nr.8 - Zakup towaru placac po 1gr - suma stu monet ma byc rowna 1zl.
    def test_nr_8_1gr_100monet(self):
        test_machine = Interface_Automatu.Tkinter()
        for i in range(0,100):
            test_machine.moneta(0.01)
        test_machine.przycisk(48)
        test_machine.przycisk_tak()
        self.assertEqual(test_machine.obliczam_roznice(), '0.0')
        
    #Test dodatkowy
    def test_nr_9_dodatkowy(self):
        test_machine = Interface_Automatu.Tkinter()
        with self.assertRaises(Wyjatki.BladNumeruLubBrakProduktu):
            test_machine.przycisk(10)
            test_machine.przycisk_tak()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
