from abc import ABC, abstractmethod

# -------------------------------
# ABSTRAKTNÉ ROZHRANIA
# -------------------------------

class Zvuk(ABC):  # Abstraktná trieda (rozhranie) pre zvuk
    def __init__(self, text_zvuku):  # Konštruktor – nastavuje konkrétny zvuk
        self._zvuk = text_zvuku

    @abstractmethod
    def urob_zvuk(self):
        pass


class Zviera(ABC):  # Abstraktná trieda pre zvieratá

    ID = 0

    def __init__(self, meno, vek):
        self.__meno = meno
        self.__vek = vek
        self.__myID = Zviera.get_ID()

    @staticmethod
    def get_ID():
        Zviera.ID += 1
        return Zviera.ID

    @property
    def meno(self):
        return self.__meno

    @meno.setter
    def meno(self, m):
        if not m:
            raise ValueError("Meno nesmie byť prázdne")
        self.__meno = m.capitalize()

    @property
    def vek(self):
        return self.__vek

    @vek.setter
    def vek(self, v):
        if v <= 0:
            raise ValueError("Vek musí byť kladný")
        self.__vek = v

    def __str__(self):
        return f"myID={self.__myID} meno={self.__meno} vek={self.__vek}"

    def __del__(self):
        print(f"{self.__meno} umieram")

    @abstractmethod
    def vykonaj(self):
        pass


# -------------------------------
# IMPLEMENTÁCIE ZVIERAT
# -------------------------------

class Pes(Zviera, Zvuk):
    def __init__(self, meno, vek, zvuk="woof woof"):
        Zviera.__init__(self, meno, vek)
        Zvuk.__init__(self, zvuk)

    def vykonaj(self):
        print(f"{self.meno} aportuje a robí zvuk: {self.urob_zvuk()}")

    def urob_zvuk(self):
        return self._zvuk


class Macka(Zviera, Zvuk):
    def __init__(self, meno, vek, zvuk="meow meow"):
        Zviera.__init__(self, meno, vek)
        Zvuk.__init__(self, zvuk)

    def vykonaj(self):
        print(f"{self.meno} loví a robí zvuk: {self.urob_zvuk()}")

    def urob_zvuk(self):
        return self._zvuk

Zviera.ID
Zviera.ID += 1
Zviera.ID

#z = Zviera('Zver', 20000)
#print(z)
p = Pes('Lajci', 5)
m = Macka('Jahoda', 5, 'mnau mnau')
p.vykonaj()
m.vykonaj()
print(p)
print(m)
print(p.urob_zvuk(), m.urob_zvuk())

Pes.mro()

#print(p.get_meno())
print(p.meno)
#p.set_meno('ORECH')
p.meno = 'ORECH'
print(p.meno)


print(p.vek)
#p.set_meno('ORECH')
p.vek = 10
print(p.vek)

# -------------------------------
# ÚTULOK
# -------------------------------

class Utulok:
    def __init__(self):
        self.zvierata = []

    def pridaj(self, zviera):
        if isinstance(zviera, Zviera) and isinstance(zviera, Zvuk):
            self.zvierata.append(zviera)
        else:
            raise TypeError("Do útulku môžeš pridať len objekt typu Zviera + Zvuk.")

    def __str__(self):
        return "Zvieratá v útulku: " + ", ".join(z.meno for z in self.zvierata)

    def vykonaj(self):
        for zviera in self.zvierata:
            zviera.vykonaj()

    def odstran(self, meno):
        for zviera in self.zvierata:
            if zviera.meno.lower() == meno.lower():
                self.zvierata.remove(zviera)
                del zviera
                print(f"Zviera s menom {meno} bolo odstránené z útulku.")
                return
        print(f"Zviera s menom {meno} sa nenašlo v útulku.")


# -------------------------------
# DEMO / TEST
# -------------------------------


utulok = Utulok()

# Zvieratá s referenciou
pes1 = Pes("Rex", 3)
macka1 = Macka("Luna", 2)

# Pridanie zvierat s referenciou
utulok.pridaj(pes1)
utulok.pridaj(macka1)

# Pridanie zvierat bez samostatnej referencie – jediné miesto, kde existujú, je v útulku
utulok.pridaj(Pes("Falko", 5, "haf haf"))
utulok.pridaj(Macka("Micka", 4, "mňau"))

print(utulok)
utulok.vykonaj()

# Odstránenie zvierat bez referencie – objekt sa zmaže a vypíše "umieram"
utulok.odstran("Micka")
utulok.odstran("Falko")

print(utulok)