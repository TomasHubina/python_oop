class Zviera:
  ID = 0

  def __init__(self, m, v):
    # self.__meno = None
    # self.__vek = None
    self.set_meno(m)
    self.set_vek(v)
    self.set_zvuk(None)
    Zviera.ID += 1
    self.__mojeID = f'Z:{Zviera.ID:02}'

  def get_meno(self):
    return self.__meno

  def get_vek(self):
    return self.__vek

  # zvuk nie je private ale protected, inak by sme ho nemohli priamo pouzivat v jeho potomkoch
  def set_zvuk(self, z):
        self._zvuk = z

  def set_meno(self, m):
    if m == '':
      raise ValueError('Meno nesmie byť prázdne')

    self.__meno = m[0].upper() + m[1:].lower()

  def set_vek(self, v):
    #if not isinstance(v, float)

    if type(v) not in [float, int]:
      raise ValueError('Zadaj číslo!')
    elif v <= 0:
        raise ValueError('Vek musí byť väčší ako nula!')
    self.__vek = v

  def info(self):
    return f"{self.__class__.__name__}: id='{self.__mojeID}' meno='{self.__meno}', vek='{self.__vek}', zvuk='{self._zvuk}' "

  def __str__(self):
    return self.info()

  def urob_zvuk(self):
        return self._zvuk



import random

class Pes(Zviera):
  # neexistuje tu tzv. overloading, nie je možné vytvoriť viac ako jeden konštruktor __init__
  def __init__(self, m, v, p=None):
    # zavolám konšturktor predka
    super().__init__(m, v)
    self.set_zvuk('Hav hav')
    self.__poslusnot = p if p is not None else random.randrange(10)

  def aport(self):
    h = random.randint(1, 10)
    if self.__poslusnot > h:
      return 'Aportujem.'
    else:
      return 'Nechce sami aportovat.'

  # polymofizmus = prekrývam metódu predka
  def info(self):
    #zvuk viem pouzit priamo v potomkoch
    return super().info() + f" poslusnost='{self.__poslusnot}' zvuk='{self._zvuk}'"

  def urob_zvuk(self):
    return super().urob_zvuk()

  def stekaj(self):
    return self.urob_zvuk()



class Macka(Zviera):
  # neexistuje tu tzv. overloading, nie je možné vytvoriť viac ako jeden konštruktor __init__
  def __init__(self, m, v):
    # zavolám konšturktor predka
    super().__init__(m, v)
    self.set_zvuk('Mnau mnau')
    self.__nezavislost = random.uniform(0.5, 1.0)

  def lov(self):
    h = random.randrange(100)
    sanca = random.random() *  self.__nezavislost
    return 'Lovim.' if sanca > 0.5 else 'Nelovim'

  # polymofizmus = prekrývam metódu predka
  def info(self):
    return super().info() + f"nezavislost='{round(self.__nezavislost, 4)}' zvuk='{self._zvuk}'"

  def urob_zvuk(self):
    return self._zvuk

  def mnaukaj(self):
    return self.urob_zvuk()


class Slon(Zviera):
  def __init__(self, m, v, d, z = None):
    super().__init__(m, v)
    self.__chobot = d
    self._zvuk = 'tuuut' if z == None else z

  def info(self):
    return super().info() + f"chobot='{self.__chobot}' zvuk='{self._zvuk}'"

  def zatrub(self):
    return self._zvuk

  def get_chobot(self):
    return self.__chobot

  def zaslapni(self, p):
    print(p, 'zasliapnuty')
    del p

z=Zviera('tapka', 6)
print("print(z): ", z)

p=Pes('TAPKA', 3)
print("print(p): ", p)

m=Macka('Cica', 5)

p.set_vek(5)
p.set_zvuk('woof')
print("print(p): ", p)
print("print(m): ", m)

s1 = Slon('Dumbo', 15, 1.5, 'tuut tuut')
s2 = Slon('Bumbo', 15, 2.0)
print("print(s1.info()): ", s1.info())
print("print(s2.info()): ", s2.info())
print("s1.zaslapni(p):")
s1.zaslapni(p)
print("print(p): ", p)
print("--------------------------------------")
class Utulok():
  def __init__(self):
    self.zvierata = []

  def pridaj(self, zviera):
    self.zvierata.append(zviera)

  def odober(self, zviera = None):
    kto = self.zvierata[-1] if zviera == None else zviera
    self.zvierata.remove(kto)

  def zaspievaj(self):
    spev = ''
    for zvieratko in self.zvierata:
      spev += zvieratko._zvuk + ' '
    return spev

  def vykonaj(self):
    for zvieratko in self.zvierata:
     if isinstance(zvieratko, Pes):
       print(zvieratko.aport())
     if isinstance(zvieratko, Macka):
       print(zvieratko.lov())
     if isinstance(zvieratko, Slon):
       print(zvieratko.zatrub())

  def zoznam_mien(self):
    zoznam = []
    for zvieratko in self.zvierata:
      zoznam.append(zvieratko.get_meno())
    return zoznam

  def __str__(self):
    return " ".join(self.zoznam_mien())

u = Utulok()
u.pridaj(p)
u.pridaj(s1)
u.pridaj(s2)
u.pridaj(m)
u.pridaj(Pes('Punto', 1))
print(u.zoznam_mien())
print(u)
print(u.zaspievaj())
u.vykonaj()
print("-------------------------")
print(u)
u.odober(s1)
print(u)
print(s1)
u.odober()
print(u)
print("-------------------------")

class Lovec:
    def lov(self):
        return f"{self.meno} sa snaží loviť."

class Zviera:
    def __init__(self, meno):
        self.meno = meno

    def urob_zvuk(self):
        return "Neznámy zvuk"

class Macka(Zviera, Lovec):
    def urob_zvuk(self):
        return "Mnau mnau"

class Pes(Zviera):
    def urob_zvuk(self):
        return "Hav hav"

pes = Pes("Rex")
macka = Macka("Micka")

print(pes.urob_zvuk())  # Hav hav
print(macka.urob_zvuk())  # Mnau mnau
print(macka.lov())  # Micka sa snaží loviť.
print(Macka.mro())  # mro() = Method Resolution Order – poradie, v akom sa hľadá metóda v prípade viacnásobného dedenia.