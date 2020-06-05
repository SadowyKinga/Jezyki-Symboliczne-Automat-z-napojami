-----------------------------------------------------------------------------------------------------
Raport
------------------------------------------------------------------------------------------------------

Przygotowanie do projektu
------------------------------------------------------------------------------------------------------
Projekt z Języków Symbolicznych -  automat z napojami, rok: 2, Informatyka, Politechnika Krakowska.
Pracowałam zarówno w środowisku PyCharm jak również w IDLE (Python 3.8 32-bit). Do graficznej prezentacji automatu użyłam biblioteki Tkinter. 
         
Budowa 
----------------------------------------------------------------------------------------------------------
Na początku projekt pisałam jako jeden plik, nie dzieląc go na moduły, gdyż było mi w ten sposób wygodniej. Jednak na końcu stwierdziłam, że należy go podzielić na kilka modułów, by spełniał kryteria dotyczące projektu.
 Projekt podzieliłam następująco: 
   
   *na główny plik o nazwie Interface_Automatu;
     
   *na plik Wyjatki;
     
   *oraz na moduł System_Automatu;
     
   *także osobno zrobiłam testy jednostkowe, by pokazać, iż program spełnia wymagania zawarte w opisie projektu.
     
 W pliku Interface_Automatu, zajmuje się logika interfacu tego automatu. Posiada on metody potrzebne do przeprowadzonych testów, wizualnie przedstawia automat, oraz odpowiada za główne odpalanie programu. Ponadto po najechaniu myszką i kliknięciu na dany produkt pokazują nam się wartości odżywcze tego produktu wraz z jego pelna nazwą jak i producentem. 
 W pliku Wyjątki są zainicjowane wyjątki, których używam następnie w interfejsie automatu.
 Natomiast w module System_Automatu, zajęłam się główna logiką Automatu. Mam tu na myśli, iż dzięki klasie Monety mogę przechowywać monety - nominały. Metody, które w niej zawarłam pozwalają na dodawanie monety do tzw. "skarbca monet" oraz na zwrot reszty gotówki za wybrany i opłacony już produkt. Dzięki klasie Produkty przechowuję numery danych produktów wraz z cenami i ich ilością. Metody, które w niej zawarłam pozwalają na sprawdzenie ceny, oraz ilości dostępności produktu. Odwołując się do klasy ObslugaAutomatu mogę sprawdzić dostępność danego produktu, jak również po zakupie wybranego usunąć go z listy asortymentu oraz obliczyć resztę potrzebną, bądź też nie potrzebną do wydania za zapłacony napój. Tutaj również dodaje możliwość by automat sam generował czy ma możliwość wydania reszty za opłacony napój, czy tez zwróci klarowny komunikat „Proszę wrzucić tylko odliczoną kwotę!” – związane jest to z wyczerpaniem już monet do wydania za zakup towaru. 
  W testach jednostkowych pozwalam sobie na:
   
   *sprawdzanie ceny produktu, który wybraliśmy, 
    
   *sprawdzenie poprawność działania kodu, gdy wrzucimy kwotę odliczona do automatu - brak reszty, 
    
   *sprawdzenie poprawność działania kodu, gdy wrzucimy kwotę większa od spodziewanej - wydawana reszta,
    
   *test dzięki któremu wykupimy cały dany produkt z asortymentu – informacja o braku produktu w automacie,
    
   *test sprawdzający ceny towarów o nieprawidłowym numerze – informacja o błędzie, 
    
   *test pozwalający na wrzucenie kilku monet a następnie przerwanie transakcji – zwrot gotówki, 
    
   *test, w którym pokażemy możliwość wrzucenia za małej kwoty, wybraniu produktu, dorzucenia reszty odliczonej kwoty oraz ponownego wybrania numeru – brak reszty, 
    
   *test, dzięki któremu pokażemy, iż za dany produkt możemy zapłacić moneta 1-groszową - przykładowo 100 monet po 1gr. 

Moja realizacja 
----------------------------------------------------------------------------------------------------------
Myślę, ze zrealizowałam wszystkie założenia dotyczące projektu. Automat pozwala na wybranie kodu, zapłatę za niego, zarówno kwotą odliczona jaki z możliwością wydania reszty gotówki. Gdy nieprawidłowo wpiszemy kod produktu na ekranie pokaże się nam informacja o błędnym numerze, natomiast gdy dany produkt już został wyczerpany dostaniemy informacje o braku dostępności towaru. Jeśli już zdecydujemy się na dany napój oraz wrzucimy pieniądze, lecz zdecydujemy na zmianę wybranego napoju należy nacisnąć czerwony przycisk X, który pozwala na przerwanie transakcji i oddanie nam wrzuconej już kwoty. Gdy wrzucimy za mało monet dostaniemy komunikat o tym, ile pozostało nam do zapłaty za dany towar . Testy, które powinny zostać przeprowadzone są udokumentowane w pliku Testy – jeśli któryś z testów by nie został spełniony widniało by przy nim słowo ERROR – oznaczające błąd, bądź tez FAIL – oznaczające przerwanie wykonywania testów, zakończone niepowodzeniem. W moim projekcie przy każdym z testów widnieje napis ok – który, oznacza iż  zarówno testy są przeprowadzone prawidłowo jak i kod działa poprawnie. Link do testów: [Tutaj link, do testów jednostkowych](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/master/Testy.py)

Dodane elementy specjalne 
----------------------------------------------------------------------------------------------------------
Elementami specjalnymi użytymi w programie są fotografie do wizualnego przedstawienia prawdziwego automatu, dzięki którym doskonale wiemy i widzimy co zamawiamy i czego należy sie spodziewać - firma danego produktu, smak, pojemność

Napotkane problemy
----------------------------------------------------------------------------------------------------------
Uważam, iż nie miałam większych problemów z realizacją tego projektu. Jedynymi jeśli mogę tak nazwać problemami były testy. Nie bardzo wiedziałam jak je udokumentować, by spełniały kryteria projektu – czy miałyby być to screeny z pokazanymi kolejno poleceniami jak działa kod, czy konkretna dokumentacja – opis. Ostatecznie postanowiłam poczytać więcej zarówno w książkach jak i Internecie o testach jednostkowych – które używane są w profesjonalnych kodach. Moja mobilizacja i chęć zagłębienia się w tę kwestię doprowadziła do napisania właśnie takich testów, dzięki którym pokazałam, iż kod działa prawidłowo. 



Linki do wymaganych w projekcie konstrukcji
----------------------------------------------------------------------------------------------------------

a. Lambda - wyrażenia:

  •[Obsługa przycisków do wrzucania monet](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/9607c7380520fbf3d227f48afffa1df6061dbac0/Interface_Automatu.py#L216)
  
  •[Obsługa przycisków do wyboru numeru produktu](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/9607c7380520fbf3d227f48afffa1df6061dbac0/Interface_Automatu.py#L231)
  
  •[Obsługa przycisków - opis danego produktu](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/4d64a91f1603fd5477cfa3827a172737166c2094/Interface_Automatu.py#L276)
  
	
b. Klasy:

  •[Klasa odpowiedzialna za interfejs użytkownika](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/9607c7380520fbf3d227f48afffa1df6061dbac0/Interface_Automatu.py#L12)
  
  •[Klasa Monety](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/668ee6f867836443564de900ba5575825f714c38/Automat%20z%20napojami.py#L12)
  
  •[Klasa Produkty](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/668ee6f867836443564de900ba5575825f714c38/Automat%20z%20napojami.py#L40)
  
  •[Klasa realizująca funkcjonalność programu - Obsluga_Automatu](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/668ee6f867836443564de900ba5575825f714c38/Automat%20z%20napojami.py#L65)
		
c. Wyjątki:

  •[Wyjątki - błędny numer, produkt wyprzedany, błędny numer lub produkt wyprzedany](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/master/Wyjatki.py)
		
d. Moduły:

  •[Import modułu System_Automaty, Wyjątki do pliku Interface_Automatu.py](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/668ee6f867836443564de900ba5575825f714c38/Interface_Automatu.py#L2)
  
  •[Import modułu System_Automatu, Interface_Automatu, Wyjatki do pliku Testy.py](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/668ee6f867836443564de900ba5575825f714c38/Testy.py#L2)
  
  •[Import modułu Wyjatki do pliku System_Automatu.py](https://github.com/SadowyKinga/Jezyki-Symboliczne-Automat-z-napojami/blob/668ee6f867836443564de900ba5575825f714c38/System_Automatu.py#L3)
