class PrvaUloha:
    def __init__(self, roky):
        self.roky = roky
    
    def usporiadaj(self):
        return sorted(self.roky, key=lambda x: x % 100)


class DruhaUloha:
    def __init__(self, slova, kriterium):
        self.slova = slova
        self.kriterium = kriterium
    
    def usporiadaj(self):
        kriteria = [lambda x: x, lambda x: x[::-1], lambda x: len(x)]
        return sorted(self.slova, key=kriteria[self.kriterium])


class TretiaUloha:
    def __init__(self, nazov_suboru, cislo_otazky):
        self.nazov_suboru = nazov_suboru
        self.cislo_otazky = cislo_otazky
    
    def spocitaj_neutralne(self):
        with open(self.nazov_suboru, "r") as subor:
            return sum(1 for riadok in subor if riadok.split(";")[self.cislo_otazky] == "3")


class StvrtaUloha:
    def __init__(self, cislo):
        self.cislo = cislo
    
    def vypocitaj(self):
        vysledok = 1
        for cifra in str(self.cislo):
            vysledok *= int(cifra)
        return vysledok


class PiataUloha:
    def __init__(self, mena):
        self.mena = mena
    
    def filtruj_a_usporiadaj(self):
        return sorted(filter(lambda x: len(x) >= 5, self.mena), reverse=True)


def prvocislo(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

class SiestaUloha:
    def __init__(self, cisla):
        self.cisla = cisla
    
    def filtruj_prvocisla(self):
        return list(filter(prvocislo, self.cisla))


class SiedmaUloha:
    def __init__(self, cisla):
        self.cisla = cisla
    
    def aplikuj(self):
        dvojnasobok = lambda x: x * 2
        zvysok_po_4 = lambda x: x % 4
        je_parne = lambda x: x % 2 == 0
        return [list(map(f, self.cisla)) for f in [dvojnasobok, zvysok_po_4, je_parne]]

# Test PrvaUloha
roky = list(map(int, input("Zadaj roky oddelené medzerou: ").split(",")))
u1 = PrvaUloha(roky)
print("Výsledok:", u1.usporiadaj())

# Test DruhaUloha
slova = input("Zadaj slová oddelené medzerou: ").split(",")
kriterium = int(input("Zadaj číslo kritéria (0-2): "))
u2 = DruhaUloha(slova, kriterium)
print("Výsledok:", u2.usporiadaj())

# Test TretiaUloha
nazov_suboru = input("Tretia uloha: ")
cislo_otazky = int(input())
u3 = TretiaUloha(nazov_suboru, cislo_otazky)
print(u3.spocitaj_neutralne())

# Test StvrtaUloha
cislo = int(input("štvrtá úloha: "))
u4 = StvrtaUloha(cislo)
print(u4.vypocitaj())

# Test PiataUloha
mena = input("Piata úloha: ").split(",")
u5 = PiataUloha(mena)
print(u5.filtruj_a_usporiadaj())

# Test SiestaUloha
cisla = list(map(int, input("Šiesta úloha: ").split(" ")))
u6 = SiestaUloha(cisla)
print(u6.filtruj_prvocisla())

# Test SiedmaUloha
cisla = list(map(int, input("Siedma úloha: ").split()))
u7 = SiedmaUloha(cisla)
print(u7.aplikuj())