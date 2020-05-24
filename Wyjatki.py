#----------------------- WYJATKI ---------------------------------------------
class BladNumeruLubBrakProduktu(Exception):
    """Klasy wyjatkow slużą do opisów błedów, nie kończa programu
    KLASY:
    *BladNumeruLubBrakProduktu - informuje klienta, iż najprawdopodobniej podał zly numer produktu, lub produkt został wyczerpany """
    
class BlednyNumer(Exception):
    """Klasy wyjatkow slużą do opisów błedów, nie kończa programu
    KLASY:
    *BlednyNumer - informuje klienta, iż podał niepoprawny numer produktu """
    
class ProduktWyprzedany(Exception):
    """Klasy wyjatkow slużą do opisów błedów, nie kończa programu
    KLASY:
    *ProduktWyprzedany - informuje klienta, iz dany produkt został wyprzedany."""
